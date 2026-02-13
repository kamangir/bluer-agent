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

    usage_1 = show_usage(
        [
            "@assistant",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "start assistant.",
        mono=mono,
    )

    # ---

    options = "".join(
        [
            xtra("install,", mono=mono),
            "worker",
        ]
    )

    usage_2 = show_usage(
        [
            "@assistant",
            f"[{options}]",
        ],
        "start assistant worker.",
        mono=mono,
    )

    # ----

    return "\n".join(
        [
            usage_1,
            usage_2,
        ]
    )
