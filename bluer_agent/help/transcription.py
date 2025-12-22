from typing import List

from bluer_options.terminal import show_usage, xtra


def help_validate(
    tokens: List[str],
    mono: bool,
) -> str:

    install_options = xtra("filename=<filename.wav>,install", mono=mono)

    record_options = "download,record,play,upload"

    options = "".join(
        [
            "language=en|fa",
            xtra(",verbose", mono=mono),
        ]
    )

    return show_usage(
        [
            "@agent",
            "transcription",
            "validate",
            f"[{install_options}]",
            "[-|<object-name>]",
            f"[{record_options}]",
            f"[{options}]",
        ],
        "validate agent.",
        mono=mono,
    )


help_functions = {
    "validate": help_validate,
}
