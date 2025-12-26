from typing import List

from bluer_options.terminal import show_usage, xtra


def help_generate(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,~play", mono=mono)

    return show_usage(
        [
            "@voice",
            "generate",
            f"[{options}]",
            "[-|<object-name>]",
            '"<sentence>"',
        ],
        "generate voice.",
        mono=mono,
    )


help_functions = {
    "generate": help_generate,
}
