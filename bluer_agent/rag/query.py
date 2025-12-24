from typing import Tuple, Any

from blueness import module

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def query(
    object_name: str,
    query: str,
) -> Tuple[bool, Any]:
    logger.info(f'{NAME}.query[{object_name}]("{query}")')

    logger.info("🪄")

    return True, ["void"]
