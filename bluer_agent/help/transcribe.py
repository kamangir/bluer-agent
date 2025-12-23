from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_agent.help.audio import record_args


def help(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("filename=<filename.wav>,install", mono=mono),
            "language=en|fa",
        ]
    )

    record_options = xtra("download,~record,~play,upload", mono=mono)

    return show_usage(
        [
            "@agent",
            "transcribe",
            f"[{options}]",
            "[-|<object-name>]",
            f"[{record_options}]",
        ]
        + record_args,
        "validate transcription.",
        mono=mono,
    )
