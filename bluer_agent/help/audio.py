from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_agent import env
from bluer_agent.transcription.functions import list_of_languages

audio_properties_args = [
    "[--channels <1>]",
    "[--crop_silence <0>]",
    "[--length <30>]",
    "[--rate <16000>]",
]


def help_converse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,", mono=mono),
            "",
            xtra(",upload", mono=mono),
        ]
    )

    args = sorted(
        [
            '[--audio_prompt "some text"]',
            "[--language {}]".format(" | ".join(list_of_languages)),
        ]
        + audio_properties_args
    )

    return show_usage(
        [
            "@audio",
            "converse",
            f"[{options}]",
            "[{} | <context-object-name>]".format(
                env.BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT
            ),
            "[-|<object-name>]",
        ]
        + args,
        "have a conversation based on the context.",
        mono=mono,
    )


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@audio",
            "install",
        ],
        "install audio.",
        mono=mono,
    )


def help_play(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("download,filename=<audio.wav>", mono=mono)

    return show_usage(
        [
            "@audio",
            "play",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "play <object-name>/<audio.wav>.",
        mono=mono,
    )


def help_record(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("filename=<audio.wav>,", mono=mono),
            "play",
            xtra(",upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@audio",
            "record",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + audio_properties_args,
        "record <object-name>/<audio.wav>.",
        mono=mono,
    )


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@audio",
            "test",
        ],
        "test audio.",
        mono=mono,
    )


help_functions = {
    "converse": help_converse,
    "install": help_install,
    "play": help_play,
    "record": help_record,
    "test": help_test,
}
