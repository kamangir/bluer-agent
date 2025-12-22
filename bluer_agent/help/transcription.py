from typing import List

from bluer_options.terminal import show_usage, xtra


def help(
    tokens: List[str],
    mono: bool,
) -> str:
    install_options = xtra("filename=<filename.wav>,install", mono=mono)

    record_options = xtra("download,~record,~play,upload", mono=mono)

    options = "".join(
        [
            "language=en|fa",
            xtra(",verbose", mono=mono),
        ]
    )

    return show_usage(
        [
            "@agent",
            "transcribe",
            f"[{install_options}]",
            "[-|<object-name>]",
            f"[{record_options}]",
            f"[{options}]",
        ],
        "validate agent.",
        mono=mono,
    )
