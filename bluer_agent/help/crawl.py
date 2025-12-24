from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help_collect(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "root=<url>,upload"
    args = [
        "[--page-count 25]",
        "[--max-depth 2]",
        "[--timeout 15.0]",
        "[--max-retries 4]",
        "[--backoff-base 0.7]",
        "[--backoff-jitter 0.4]",
        "[--delay 0.2]",
    ]

    return show_usage(
        [
            "@crawl",
            "collect",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "crawl <root> -> <object-name>.",
        mono=mono,
    )


def help_review(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "download"

    return show_usage(
        [
            "@crawl",
            "review",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "review <object-name>.",
        mono=mono,
    )


help_functions = {
    "collect": help_collect,
    "review": help_review,
}
