from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_agent.help.audio import audio_properties_args
from bluer_agent.transcription.functions import list_of_languages


def help(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("download,filename=<filename.wav>,install,", mono=mono),
            "play",
            xtra(",upload", mono=mono),
        ]
    )

    args = sorted(
        [
            "[--language {}]".format(" | ".join(list_of_languages)),
            "[--record 0]",
        ]
        + audio_properties_args
    )

    return show_usage(
        [
            "@transcribe",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "validate transcription.",
        mono=mono,
    )
