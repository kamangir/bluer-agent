from __future__ import annotations

from typing import Any, List, Tuple
from flask import render_template_string, session
from dataclasses import dataclass

from bluer_options.timing import ElapsedTimer
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.mlflow.tags import set_tags

from bluer_agent import env
from bluer_agent import ALIAS, ICON, VERSION
from bluer_agent.assistant.classes.conversation.list_of import List_of_Conversations
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.functions import template
from bluer_agent.assistant.classes.interaction import Interaction
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.host import signature
from bluer_agent.logger import logger


@dataclass
class GuiElements:
    index_display: str = " - "
    can_delete: bool = False
    can_next: bool = False
    can_prev: bool = False


class Conversation:
    def __init__(self):
        self.object_name = ""

        self.list_of_interactions: List[Interaction] = []

        self.subject: str = ""

    def get_gui_elements(
        self,
        index: int,
        reply_id: str,
    ) -> Tuple[Any, GuiElements]:
        list_of_interactions = self.get_list_of_interactions(
            reply_id=reply_id,
        )

        if len(list_of_interactions) == 0:
            logger.warning(f"interaction not found: index={index}, reply={reply_id}")
            return None, GuiElements()

        gui_elements = GuiElements(
            can_delete=True,
        )

        index = max(min(index, len(list_of_interactions) - 1), 0)

        interaction = (
            list_of_interactions[index]
            if 0 <= index < len(list_of_interactions)
            else None
        )

        gui_elements.can_prev = index > 0

        gui_elements.can_next = 0 <= index < len(list_of_interactions) - 1

        gui_elements.index_display = f"{index + 1} / {len(list_of_interactions)}"

        return interaction, gui_elements

    def get_list_of_interactions(
        self,
        reply_id: str = "top",
    ) -> List[Interaction]:
        if reply_id == "top":
            return self.list_of_interactions

        for interaction in self.list_of_interactions:
            for reply in interaction.list_of_replies:
                if reply.id == reply_id:
                    return reply.list_of_interactions

        return []

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

        logger.info(
            "{}: {} interaction(s) loaded from {}".format(
                convo.__class__.__name__,
                len(convo.list_of_interactions),
                convo.object_name,
            )
        )

        return convo

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

        return render_template_string(
            template_text,
            # main view
            interaction=interaction,
            gui_elements=gui_elements,
            index=index + 1,
            object_name=self.object_name,
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
            title=f"{ICON} {ALIAS}-{VERSION}",
            subject=self.subject,
            selected_item="question",
            # sidebar
            list_of_conversations=list_of_conversations.contents,
            conversation_count=len(list_of_conversations.contents),
            active_object_name=self.object_name,
        )

    def save(
        self,
        tag: bool = True,
    ) -> bool:
        filename = objects.path_of(
            object_name=self.object_name,
            filename="conversation.dat",
        )

        if not file.save(
            filename,
            self,
            log=True,
        ):
            return False

        if tag and not set_tags(
            object_name=self.object_name,
            tags="convo",
            verbose=verbose,
        ):
            return False

        logger.info(
            "{}: {} interaction(s) saved to {}".format(
                self.__class__.__name__,
                len(self.list_of_interactions),
                self.object_name,
            )
        )

        return True
