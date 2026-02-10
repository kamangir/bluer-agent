from __future__ import annotations

from typing import Any, List, Tuple
from flask import render_template_string, session

from bluer_objects import objects
from bluer_objects.mlflow.tags import set_tags
from bluer_objects.metadata import post_to_object, get_from_object

from bluer_agent import env
from bluer_agent.assistant.env import verbose
from bluer_agent.host import signature
from bluer_agent import ALIAS, ICON, VERSION
from bluer_agent.assistant.functions import template
from bluer_agent.assistant.classes.archive import Archive
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

    def compute_view_state(self, index: int) -> Tuple[Any, bool, bool, str]:
        item = self.history[index] if 0 <= index < len(self.history) else None

        can_prev = index > 0

        can_next = 0 <= index < len(self.history) - 1

        idx_display = (
            "0 / 0" if len(self.history) == 0 else f"{index + 1} / {len(self.history)}"
        )

        return item, can_prev, can_next, idx_display

    @staticmethod
    def load(object_name: str) -> "Conversation":
        convo = Conversation()
        convo.object_name = object_name

        metadata = get_from_object(
            object_name,
            "convo",
            {},
        )
        assert isinstance(metadata, dict)

        convo.history = metadata.get("history", [])
        convo.subject = metadata.get("subject", "")

        # normalize
        if not isinstance(convo.history, list):
            logger.warning(
                "history is expected to be a list, was a {}.".format(
                    convo.history.__class__.__name__,
                )
            )
            convo.history = []

        logger.info(
            "{}: {} interaction(s) loaded from {}".format(
                convo.__class__.__name__,
                len(convo.history),
                convo.object_name,
            )
        )

        return convo

    @staticmethod
    def render(
        object_name: str,
        index: int,
    ) -> str:
        template_text = template.load()
        if not template_text:
            return "❗️ app.html not found."

        if "archive" not in session:
            session["archive"] = objects.path_of(
                object_name=object_name,
                filename="archive.yaml",
            )
        archive = Archive(session["archive"])

        convo = Conversation.load(object_name)

        if index < 0 and convo.history:
            index = 0

        item, can_prev, can_next, idx_display = convo.compute_view_state(index)

        return render_template_string(
            template_text,
            # main view
            item=item,
            can_prev=can_prev,
            can_next=can_next,
            idx_display=idx_display,
            object_name=convo.object_name,
            signature=" | ".join(
                [f"model: {env.BLUER_AGENT_CHAT_MODEL_NAME}"] + signature()
            ),
            title=f"{ICON} {ALIAS}-{VERSION}",
            subject=convo.subject,
            # sidebar
            conversations=archive.list_of,
            conversation_count=len(archive.list_of),
            active_object_name=convo.object_name,
        )

    def save(self):
        post_to_object(
            object_name=self.object_name,
            key="convo",
            value={
                "history": self.history,
                "subject": self.subject,
            },
        )

        set_tags(
            object_name=self.object_name,
            tags="convo",
            verbose=verbose,
        )

        logger.info(
            "{}: {} interaction(s) saved to {}".format(
                self.__class__.__name__,
                len(self.history),
                self.object_name,
            )
        )
