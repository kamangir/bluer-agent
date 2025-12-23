from blueness import module

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def play(arg: str) -> bool:
    logger.info(f"{NAME}.play: arg={arg}")
    return True
