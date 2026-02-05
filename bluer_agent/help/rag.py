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
            "[.|<crawl-object-name>]",
            "[-|<corpus-object-name>]",
        ]
        + args,
        "build rag.",
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
            "<query>",
            "[-|<query-object-name>]",
        ],
        "query <query> on <corpus-object-name> -> <query-object-name>.",
        mono=mono,
    )


help_functions = {
    "build_corpus": help_build_corpus,
    "query": help_query,
}
