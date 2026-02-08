from typing import List

from bluer_options.terminal import show_usage


def help_(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "upload"

    args = [
        "[--filename <report.html>]",
        "[--prompt <prompt>]",
        "[--remove_thoughts 1]",
    ]

    return show_usage(
        [
            "@chat",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "validate chatting.",
        mono=mono,
    )


help_functions = {
    "": help_,
}
