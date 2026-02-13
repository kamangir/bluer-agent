from typing import List
from tqdm import tqdm
from dataclasses import dataclass
from flask import render_template_string

from bluer_options.logger.config import log_list
from bluer_options.timing import ElapsedTimer
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.mlflow.tags import search

from bluer_agent import env
from bluer_agent import ICON
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.functions import template
from bluer_agent.host import signature
from bluer_agent.logger import logger


@dataclass
class Entry:
    object_name: str
    subject: str


class List_of_Conversations:
    def __init__(self):
        self.filename = objects.path_of(
            object_name=env.BLUER_AGENT_ASSISTANT_CACHE,
            filename="list_of_conversations.dat",
        )

        verb: str = "loaded"
        _, metadata = file.load(
            self.filename,
            ignore_error=True,
            default={},
        )

        if not isinstance(metadata, dict):
            logger.warning(
                "{}: dict expected, {} received.".format(
                    self.__class__.__name__,
                    metadata.__class__.__name__,
                )
            )
            metadata = {}

        self.contents: List[Entry] = metadata.get("contents", [])

        self.contents = [entry for entry in self.contents if entry.object_name]

        if not self.contents:
            verb = "found"
            _, list_of_objects = search("convo")

            logger.info("found {} object(s)".format(len(list_of_objects)))

            for object_name in tqdm(list_of_objects):
                convo = Conversation.load(object_name=object_name)

                self.append(
                    object_name,
                    convo.subject,
                )

        if verbose:
            log_list(
                logger,
                f"{self.__class__.__name__}: {verb}",
                [entry.object_name for entry in self.contents],
                "conversation(s)",
            )
        else:
            logger.info(
                "{}: loaded {} conversation(s)".format(
                    self.__class__.__name__,
                    len(self.contents),
                )
            )

        if verb == "found":
            self.save()

    def append(
        self,
        object_name: str,
        subject: str,
    ) -> "List_of_Conversations":
        self.contents.append(
            Entry(
                object_name=object_name,
                subject=subject,
            )
        )

        return self

    def generate_subject(
        self,
        convo: Conversation,
    ) -> bool:
        if not convo.generate_subject():
            return False

        self.update(
            convo.object_name,
            convo.subject,
        )

        return self.save()

    def index(self, object_name: str) -> int:
        for index, entry in enumerate(self.contents):
            if entry.object_name == object_name:
                return index
        return -1

    def render(
        self,
        convo: Conversation,
        index: int,
        reply_id: str,
    ) -> str:
        elapsed_timer = ElapsedTimer()

        template_text = template.load()
        if not template_text:
            return "❗️ app.html not found."

        interaction, gui_elements = convo.get_gui_elements(
            index=index,
            reply_id=reply_id,
        )

        return render_template_string(
            template_text,
            # main view
            interaction=interaction,
            top_interaction=convo.get_top_interaction(reply_id),
            gui_elements=gui_elements,
            index=index,
            object_name=convo.object_name,
            reply=convo.get_reply(reply_id),
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
            subject=convo.subject,
            # sidebar
            list_of_conversations=self.contents,
            conversation_count=len(self.contents),
            active_object_name=convo.object_name,
        )

    def save(self) -> bool:
        logger.info(
            "{}: saving {} conversation(s)".format(
                self.__class__.__name__,
                len(self.contents),
            )
        )

        return file.save(
            self.filename,
            {
                "contents": self.contents,
            },
            log=True,
        )

    def update(
        self,
        object_name: str,
        subject: str,
    ) -> "List_of_Conversations":
        for entry in self.contents:
            if entry.object_name == object_name:
                entry.subject = subject
                break

        return self
