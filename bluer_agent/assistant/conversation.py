from __future__ import annotations

from typing import Any, List, Tuple
from flask import render_template_string

from bluer_objects.mlflow.tags import set_tags, search
from bluer_objects.metadata import post_to_object, get_from_object

from bluer_agent.assistant.consts import verbose
from bluer_agent.host import signature
from bluer_agent import ALIAS, ICON, NAME, VERSION
from bluer_agent.assistant import template
from bluer_agent.logger import logger


class Conversation:
    def __init__(
        self,
        object_name: str = "",
    ):
        self.object_name = ""

        self.history: List[str] = []
        self.index: int = -1
        self.subject: str = ""

        if object_name:
            self.load(object_name)

    def compute_view_state(self) -> Tuple[Any, bool, bool, str]:
        item = self.history[self.index] if 0 <= self.index < len(self.history) else None

        can_prev = self.index > 0

        can_next = 0 <= self.index < len(self.history) - 1

        idx_display = (
            "0 / 0"
            if len(self.history) == 0
            else f"{self.index + 1} / {len(self.history)}"
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
        convo.index = metadata.get("index", len(convo.history) - 1)
        convo.subject = metadata.get("subject", "")

        # normalize
        if not isinstance(convo.history, list):
            logger.warning(
                "history is expected to be a list, was a {}.".format(
                    convo.history.__class__.__name__,
                )
            )
            convo.history = []

        try:
            convo.index = int(convo.index)
        except Exception:
            convo.index = len(convo.history) - 1

        logger.info(
            "{} loaded from {}".format(
                convo.__class__.__name__,
                convo.object_name,
            )
        )

        return convo

    @staticmethod
    def list_of() -> List[str]:
        return search("convo")[1]

    @staticmethod
    def render(object_name: str) -> str:
        template_text = template.load()
        if not template_text:
            return "❗️ app.html not found."

        convo = Conversation.load(object_name)

        item, can_prev, can_next, idx_display = convo.compute_view_state()

        return render_template_string(
            template_text,
            # main view
            item=item,
            can_prev=can_prev,
            can_next=can_next,
            idx_display=idx_display,
            object_name=convo.object_name,
            signature=" | ".join(signature()),
            title=f"{ICON} {ALIAS}-{VERSION}",
            subject=convo.subject,
            # sidebar
            # conversations=Conversation.list_of(),
            active_conversation_id=convo.object_name,
        )

    def save(self):
        post_to_object(
            object_name=self.object_name,
            key="convo",
            value={
                "history": self.history,
                "index": int(self.index),
                "subject": self.subject,
            },
        )

        set_tags(
            object_name=self.object_name,
            tags="convo",
            verbose=verbose,
        )

        logger.info(
            "{} saved to {}".format(
                self.__class__.__name__,
                self.object_name,
            )
        )
