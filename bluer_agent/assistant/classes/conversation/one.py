from __future__ import annotations

from typing import Any, List, Tuple, Union, Dict
from flask import render_template_string
from dataclasses import dataclass

from bluer_options.timing import ElapsedTimer
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.mlflow.tags import set_tags

from bluer_agent import env
from bluer_agent import ICON
from bluer_agent.assistant.classes.conversation.list_of import List_of_Conversations
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.functions import template
from bluer_agent.assistant.classes.interaction import Interaction, Reply
from bluer_agent.assistant.classes.conversation import get
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.host import signature
from bluer_agent.logger import logger


@dataclass
class GuiElements:
    index_display: str = " - "
    can_delete: bool = False
    can_next: bool = False
    can_prev: bool = False
    can_up: bool = False


latest_version: str = "2.00"


class Conversation:
    def __init__(self):
        self.version = latest_version

        self.object_name: str = ""

        self.list_of_interactions: List[Interaction] = []

        self.subject: str = ""

        self.metadata: Dict[str, Any] = {}

    @property
    def icon(self) -> str:
        return "({})".format(
            "".join([interaction.icon for interaction in self.list_of_interactions])
        )

    def get_gui_elements(
        self,
        index: int,
        reply_id: str,
    ) -> Tuple[Any, GuiElements]:
        logger.info(f"generating gui elements for reply={reply_id}, index={index}")

        list_of_interactions = self.get_list_of_interactions(
            reply_id=reply_id,
        )

        gui_elements = GuiElements()

        gui_elements.can_up = reply_id != "top"

        if len(list_of_interactions) == 0:
            logger.warning(f"interaction not found: index={index}, reply={reply_id}")
            return None, gui_elements

        gui_elements.can_delete = True

        index = max(min(index, len(list_of_interactions)), 1)

        interaction = (
            list_of_interactions[index - 1]
            if 1 <= index <= len(list_of_interactions)
            else None
        )

        gui_elements.can_prev = index > 1

        gui_elements.can_next = 1 <= index < len(list_of_interactions)

        gui_elements.index_display = f"{index} / {len(list_of_interactions)}"

        return interaction, gui_elements

    def generate_subject(self) -> bool:
        if not self.list_of_interactions:
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
                        self.list_of_interactions[0].question,
                    ),
                }
            ],
        )
        if not success:
            return success

        self.subject = subject
        if not self.save():
            return False

        return (
            List_of_Conversations()
            .update(
                self.object_name,
                subject,
            )
            .save()
        )

    def get_context(
        self,
        reply_id: str,
    ) -> List[Dict]:
        return Conversation.get_context_(
            owner=self,
            reply_id=reply_id,
        )

    @classmethod
    def get_context_(
        cls,
        owner: Union["Conversation", Reply],
        reply_id: str,
    ) -> List[Dict]:
        if reply_id == "top":
            return []

        for interaction in owner.list_of_interactions:
            reply_index = interaction.index_of(reply_id)
            if reply_index == -1:
                continue

            reply = interaction.list_of_replies[reply_index]
            assert isinstance(reply, Reply)

            list_of_messages = [
                {
                    "role": "user",
                    "content": interaction.question,
                },
                {
                    "role": "assistant",
                    "content": reply.content,
                },
            ]

            if reply.id == reply_id:
                return list_of_messages

            return list_of_messages + cls.get_context_(
                owner=reply,
                reply_id=reply_id,
            )

    def get_top_interaction(
        self,
        reply_id: str = "top",
    ) -> Union[Interaction, None]:
        return get.get_top_interaction(
            reply_id=reply_id,
            list_of_interactions=self.list_of_interactions,
        )

    def get_list_of_interactions(
        self,
        reply_id: str = "top",
    ) -> List[Interaction]:
        return get.get_list_of_interactions(
            reply_id=reply_id,
            list_of_interactions=self.list_of_interactions,
        )

    def get_reply(
        self,
        reply_id: str = "top",
    ) -> Union[Reply, None]:
        return get.get_reply(
            reply_id=reply_id,
            list_of_interactions=self.list_of_interactions,
        )

    def get_top_reply_id(
        self,
        reply_id: str,
    ) -> str:
        return get.get_top_reply_id(
            reply_id=reply_id,
            list_of_interactions=self.list_of_interactions,
            top_reply_id="top",
        )

    @staticmethod
    def load(
        object_name: str,
    ) -> "Conversation":
        filename = objects.path_of(
            object_name=object_name,
            filename="conversation.dat",
        )

        success, convo = file.load(
            filename,
            ignore_error=True,
            default=Conversation(),
        )

        assert isinstance(convo, Conversation)
        convo.object_name = object_name

        if not success:
            return convo

        if not isinstance(convo, Conversation):
            logger.error(
                "Conversation expected, received {}.".format(
                    convo.__class__.__name__,
                )
            )
            return Conversation()

        if not convo.migrate():
            return Conversation()

        logger.info(
            "{}: {} interaction(s) loaded from {}".format(
                convo.__class__.__name__,
                len(convo.list_of_interactions),
                convo.object_name,
            )
        )

        return convo

    def migrate(self) -> bool:
        if not hasattr(self, "version"):
            self.version = latest_version
            logger.info(f"{self.__class__.__name__}.migrate: += version")

        if not hasattr(self, "metadata"):
            logger.info(f"{self.__class__.__name__}.migrate: += metadata")
            self.metadata = {}

        return True

    def render(
        self,
        index: int,
        reply_id: str,
    ) -> str:
        elapsed_timer = ElapsedTimer()

        list_of_conversations = List_of_Conversations()

        template_text = template.load()
        if not template_text:
            return "❗️ app.html not found."

        interaction, gui_elements = self.get_gui_elements(
            index=index,
            reply_id=reply_id,
        )

        reply = self.get_reply(reply_id)

        top_interaction = self.get_top_interaction(reply_id)

        return render_template_string(
            template_text,
            # main view
            interaction=interaction,
            top_interaction=top_interaction,
            gui_elements=gui_elements,
            index=index,
            object_name=self.object_name,
            reply=reply,
            reply_id=reply_id,
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
            title=f"{ICON} @assistant",
            subject=self.subject,
            # sidebar
            list_of_conversations=list_of_conversations.contents,
            conversation_count=len(list_of_conversations.contents),
            active_object_name=self.object_name,
        )

    def save(self) -> bool:
        filename = objects.path_of(
            object_name=self.object_name,
            filename="conversation.dat",
        )

        if not file.save(
            filename,
            self,
            log=verbose,
        ):
            return False

        tagged_log: str = ""
        if self.metadata.get("tagged", False):
            if not set_tags(
                object_name=self.object_name,
                tags="convo",
                verbose=verbose,
            ):
                return False

            self.metadata["tagged"] = True
            tagged_log = " and tagged"

        logger.info(
            "{}: {} interaction(s) saved to {}{}".format(
                self.__class__.__name__,
                len(self.list_of_interactions),
                self.object_name,
                tagged_log,
            )
        )

        return True
