from typing import List
from tqdm import tqdm
from flask import session
from dataclasses import dataclass

from bluer_options.logger.config import log_list
from bluer_objects import file
from bluer_objects.mlflow.tags import search
from bluer_objects.metadata import get_from_object

from bluer_agent.assistant.env import verbose
from bluer_agent.logger import logger


@dataclass
class Entry:
    object_name: str
    subject: str


class List_of_Conversations:
    def __init__(
        self,
        filename: str = "",
    ):
        self.filename = filename
        if not self.filename:
            if "list_of_conversations" not in session:
                session["list_of_conversations"] = file.auxiliary(
                    object_name="auxiliary",
                    nickname="list_of_conversations",
                    extension="dat",
                )

            self.filename = session["list_of_conversations"]

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
                metadata = get_from_object(
                    object_name,
                    "convo",
                    {},
                )
                try:
                    self.append(
                        object_name,
                        metadata["subject"],
                    )
                except Exception as e:
                    logger.warning(e)

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

    def index(self, object_name: str) -> int:
        for index, entry in enumerate(self.contents):
            if entry.object_name == object_name:
                return index
        return -1

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
