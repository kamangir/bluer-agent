from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_agent import env


def help_assistant(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra(
        f"download,~open,port=<{env.BLUER_AGENT_ASSISTANT_PORT}>,upload",
        mono=mono,
    )

    return show_usage(
        [
            "@assistant",
            f"[{options}]",
            f"[{env.BLUER_AGENT_ASSISTANT_OBJECT}|<object-name>]",
        ],
        "start assistant.",
        mono=mono,
    )
