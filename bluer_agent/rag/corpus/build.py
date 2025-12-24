from blueness import module

from bluer_plugin import NAME
from bluer_plugin.logger import logger


NAME = module.name(__file__, NAME)


def build(object_name: str) -> bool:
    logger.info(f"{NAME}.build({object_name})")

    logger.info("🪄")

    return True
