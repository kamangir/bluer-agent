from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_agent import env


def help_assistant(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra(
                f"download,install,~open,port=<{env.BLUER_AGENT_ASSISTANT_PORT}>,upload,",
                mono=mono,
            ),
            "worker",
        ]
    )

    return show_usage(
        [
            "@assistant",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "start assistant.",
        mono=mono,
    )
