from typing import List, Tuple
from tqdm import tqdm

from bluer_options.logger.config import log_list
from bluer_objects import file
from bluer_objects.mlflow.tags import search
from bluer_objects.metadata import get_from_object

from bluer_agent.logger import logger


class Archive:
    def __init__(
        self,
        filename: str,
    ):
        self.filename = filename

        verb: str = "loaded"
        _, metadata = file.load_yaml(
            filename,
            ignore_error=True,
            default={},
        )

        assert isinstance(metadata, dict)
        self.history: List[List[str, str]] = metadata.get("history", [])

        self.history = [pair for pair in self.history if pair[0]]

        if not self.history:
            verb = "found"
            success, list_of_objects = search("convo")
            assert success

            logger.info("found {} object(s)".format(len(list_of_objects)))

            for object_name in tqdm(list_of_objects):
                metadata = get_from_object(object_name, "convo", {})
                try:
                    self.history.append([object_name, metadata["subject"]])
                except Exception as e:
                    logger.warning(e)

        log_list(
            logger,
            f"{self.__class__.__name__}: {verb}",
            [pair[0] for pair in self.history],
            "conversation(s)",
        )

        if verb == "found":
            self.save()

    def save(self) -> bool:
        logger.info(
            "{}: saving {} conversation(s)".format(
                self.__class__.__name__,
                len(
                    self.history,
                ),
            )
        )

        return file.save_yaml(
            self.filename,
            {
                "history": self.history,
            },
        )
