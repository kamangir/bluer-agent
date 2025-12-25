from blueness import module

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def embed(
    corpus_object_name: str,
) -> bool:
    logger.info(f"{NAME}.embedding {corpus_object_name} ...")

    logger.info("🪄")

    return True
