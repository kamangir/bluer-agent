from blueness import module

from bluer_options import string
from bluer_options.host import is_rpi
from bluer_objects import file, objects
from bluer_objects.host import shell

from bluer_agent import NAME
from bluer_agent.audio import consts
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def listen(
    object_name: str,
    filename: str = "audio.wav",
    length: int = 30,  # in seconds
    rate: int = 48000,
    channels: int = 1,
) -> bool:
    full_filename = objects.path_of(
        object_name=object_name,
        filename=filename,
    )

    logger.info(
        "{}.listen: {}/{} @ max: {}, sample rate: {}, {} channel(s) ... (^C to end)".format(
            NAME,
            object_name,
            filename,
            string.pretty_duration(length),
            rate,
            channels,
        )
    )

    # input device:
    # - On Raspberry Pi with mic as default: don't specify device
    # - If you need a specific ALSA device: add `-t alsa hw:1,0` after rec
    if not shell(
        [
            "rec",
            "-V1",
            f'-r "{rate}"',
            f'-c "{channels}"',
            full_filename,
            f"trim 0 {length}",
            "silence",
            f'1 "{consts.BLUER_AGENT_AUDIO_LISTEN_START_HOLD}" "{consts.BLUER_AGENT_AUDIO_LISTEN_START_THRESHOLD}',
            f'1 "{consts.BLUER_AGENT_AUDIO_LISTEN_STOP_HOLD}" "{consts.BLUER_AGENT_AUDIO_LISTEN_STOP_THRESHOLD}',
        ]
    ):
        return False

    if not file.exists(full_filename):
        logger.error(f"{NAME}.listen: {full_filename} does not exist.")
        return False

    logger.info(
        "audio size: {}".format(
            string.pretty_bytes(file.size(full_filename)),
        )
    )
    return True
