from typing import List

from bluer_options.terminal import show_usage, xtra


def help_validate(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~play", mono=mono)

    return show_usage(
        [
            "@voice",
            "validate",
            f"[{options}]",
        ],
        "validate voice generation.",
        mono=mono,
    )


help_functions = {
    "validate": help_validate,
}
