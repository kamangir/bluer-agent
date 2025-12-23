from blueness import module

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def listen(arg: str) -> bool:
    logger.info(f"{NAME}.listen: arg={arg}")
    return True
