from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects.metadata import get_from_object

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def build(object_name: str) -> bool:
    logger.info(f"{NAME}.build({object_name})")

    corpus_nodes = get_from_object(object_name, "corpus", [])
    log_list(logger, "loaded", corpus_nodes, "node(s)")

    logger.info("🪄")

    return True
