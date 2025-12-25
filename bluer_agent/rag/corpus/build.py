from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects.metadata import get_from_object

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def build(
    crawl_object_name: str,
    corpus_object_name: str,
) -> bool:
    logger.info(f"{NAME}.build: {crawl_object_name} -> {corpus_object_name}")

    corpus_roots = get_from_object(crawl_object_name, "corpus", [])
    log_list(logger, "loaded", corpus_roots, "root(s)")

    logger.info("🪄")

    return True
