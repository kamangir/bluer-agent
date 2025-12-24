from blueness import module

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def build(object_name: str) -> bool:
    logger.info(f"{NAME}.build({object_name})")

    logger.info("🪄")

    return True
