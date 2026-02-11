from __future__ import annotations

from typing import Any, List, Tuple
from flask import render_template_string, session

from bluer_objects import file
from bluer_objects import objects
from bluer_options.timing import ElapsedTimer
from bluer_objects.mlflow.tags import set_tags
from bluer_objects.metadata import post_to_object, get_from_object

from bluer_agent import env
from bluer_agent import ALIAS, ICON, VERSION
from bluer_agent.assistant.classes.conversation.list_of import List_of_Conversations
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.functions import template
from bluer_agent.chat.functions import chat
from bluer_agent.host import signature
from bluer_agent.logger import logger


class Conversation:
    def __init__(
        self,
        object_name: str = "",
    ):
        self.object_name = ""

        self.history: List[str] = []
        self.subject: str = ""

        if object_name:
            self.load(object_name)

    def compute_view_state(self) -> Tuple[Any, bool, bool, str]:
        if len(self.history) == 0:
            session["index"] = -1
            return None, False, False, False, "-"

        index = session["index"]
        index = max(min(index, len(self.history) - 1), 0)
        session["index"] = index

        item = self.history[index] if 0 <= index < len(self.history) else None

        can_prev = index > 0

        can_next = 0 <= index < len(self.history) - 1

        idx_display = f"{index + 1} / {len(self.history)}"

        return item, can_prev, can_next, True, idx_display

    def generate_subject(self) -> bool:
        if not self.history:
            return False

        prompt = """
This is the first question in a conversation. Generate a title for 
this conversation in the same language of the question. Do not use 
markdown symbols in the title. Do not start the title with "title:"

question: {}
"""

        success, subject = chat(
            messages=[
                {
                    "role": "user",
                    "content": prompt.format(
                        self.history[0]["input"],
                    ),
                }
            ],
        )
        if not success:
            return success

        self.subject = subject
        if not self.save(tag=False):
            return False

        return (
            List_of_Conversations()
            .update(
                self.object_name,
                subject,
            )
            .save()
        )

    def load(self, object_name: str) -> "Conversation":
        self.object_name = object_name

        metadata = get_from_object(
            object_name,
            "convo",
            {},
        )
        if not isinstance(metadata, dict):
            logger.warning(
                "{}.load: dict expected, {} received.".format(
                    self.__class__.__name__,
                    metadata.__class__.__name__,
                )
            )
            metadata = {}

        self.history = metadata.get("history", [])
        self.subject = metadata.get("subject", "")

        # normalize
        if not isinstance(self.history, list):
            logger.warning(
                "history is expected to be a list, was a {}.".format(
                    self.history.__class__.__name__,
                )
            )
            self.history = []

        logger.info(
            "{}: {} interaction(s) loaded from {}".format(
                self.__class__.__name__,
                len(self.history),
                self.object_name,
            )
        )

        return self

    def render(self) -> str:
        elapsed_timer = ElapsedTimer()

        template_text = template.load()
        if not template_text:
            return "❗️ app.html not found."

        list_of_conversations = List_of_Conversations()

        item, can_prev, can_next, can_delete, idx_display = self.compute_view_state()

        return render_template_string(
            template_text,
            # main view
            item=item,
            can_prev=can_prev,
            can_next=can_next,
            can_delete=can_delete,
            idx_display=idx_display,
            index=session["index"],
            object_name=self.object_name,
            signature=" | ".join(
                [f"model: {env.BLUER_AGENT_CHAT_MODEL_NAME}"]
                + signature()
                + [
                    "took {}".format(
                        elapsed_timer.as_str(
                            include_ms=True,
                            short=True,
                        ),
                    )
                ]
            ),
            title=f"{ICON} {ALIAS}-{VERSION}",
            subject=self.subject,
            # sidebar
            list_of_conversations=list_of_conversations.history,
            conversation_count=len(list_of_conversations.history),
            active_object_name=self.object_name,
        )

    def save(
        self,
        tag: bool = True,
    ) -> bool:
        success: bool = True

        if not post_to_object(
            object_name=self.object_name,
            key="convo",
            value={
                "history": self.history,
                "subject": self.subject,
            },
        ):
            success = False

        if tag and not set_tags(
            object_name=self.object_name,
            tags="convo",
            verbose=verbose,
        ):
            success = False

        if success:
            logger.info(
                "{}: {} interaction(s) saved to {}".format(
                    self.__class__.__name__,
                    len(self.history),
                    self.object_name,
                )
            )

        return success
