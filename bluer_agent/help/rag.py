from typing import List

from bluer_options.terminal import show_usage, xtra


def help_build_corpus(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("download,upload", mono=mono)

    args = []

    return show_usage(
        [
            "@rag",
            "build_corpus",
            f"[{options}]",
            "[.|<corpus-object-name>]",
        ]
        + args,
        "build <corpus-object-name>.",
        mono=mono,
    )


def help_query(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("download", mono=mono)

    return show_usage(
        [
            "@rag",
            "query",
            f"[{options}]",
            "[.|<corpus-object-name>]",
            "<sentence>",
        ],
        "query <sentence> against <corpus-object-name>.",
        mono=mono,
    )


help_functions = {
    "build_corpus": help_build_corpus,
    "query": help_query,
}
