from bluer_options.logger.config import log_list
from bluer_objects import file
from bluer_objects.mlflow.tags import search

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
        self.list_of = metadata.get("list_of", [])

        if not self.list_of:
            _, self.list_of = search("convo")
            verb = "found"

        log_list(
            logger,
            f"{self.__class__.__name__}: {verb}",
            self.list_of,
            "conversation(s)",
        )

        if verb == "found":
            self.save()

    def save(self) -> bool:
        return file.save_yaml(
            self.filename,
            {
                "list_of": self.list_of,
            },
        )
