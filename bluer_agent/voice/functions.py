from typing import Tuple

from blueness import module
from bluer_objects import objects

from bluer_agent import NAME
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def generate_voice(
    object_name: str,
    sentence: str,
    filename: str = "voice.mp3",
    download: bool = True,
) -> Tuple[bool, str]:
    logger.info(
        '{}.generate_voice: "{}" -{}> {}/{}'.format(
            NAME,
            sentence,
            "downloaded-" if download else "",
            object_name,
            filename,
        )
    )

    full_filename = objects.path_of(
        object_name=object_name,
        filename=filename,
    )

    logger.info("🪄")

    return True, full_filename
