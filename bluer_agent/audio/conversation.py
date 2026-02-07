import time
from typing import Tuple

from blueness import module
from bluer_objects import file
from bluer_options import string
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent.assets.path import get_path
from bluer_agent.audio.play import play
from bluer_agent.audio.properties import AudioProperties
from bluer_agent.chat.functions import chat
from bluer_agent.rag.corpus.context import Context
from bluer_agent.rag.prompt.single_root import build_prompt
from bluer_agent.transcription.functions import transcribe
from bluer_agent.voice.functions import generate_voice
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

greeting: str = "سلام، من رنگین هستم. چطور می‌تونم کمک‌تون کنم؟"


def converse(
    context: Context,
    object_name: str,
    greeting: str = greeting,
    language: str = "fa",
    audio_properties: AudioProperties = AudioProperties(),
    loop: bool = False,
) -> Tuple[bool, str, str, str]:
    logger.info(
        "{}.converse:context[{}] -{}> {}".format(
            NAME,
            context.object_name,
            "loop-" if loop else "",
            object_name,
        )
    )

    audio_prompt: str = greeting

    while True:
        html_report = HTMLReport(template=get_path("./query.html"))

        success, filename = generate_voice(
            object_name=object_name,
            sentence=audio_prompt,
        )
        if not success:
            return success, "", ""

        if not play(
            object_name=object_name,
            filename=filename,
        ):
            return False, "", ""

        time.sleep(1)

        filename = "{}.wav".format(string.timestamp())

        success, query = transcribe(
            object_name=object_name,
            filename=filename,
            language=language,
            record=True,
            properties=audio_properties,
        )
        if not success or not query:
            return success, query, ""

        success, query_context = context.generate(
            query=query,
            html_report=html_report,
        )
        if not success:
            return success, query, ""

        success, reply = chat(
            messages=build_prompt(
                query=query,
                context=query_context["chunks"],
            ),
            html_report=html_report,
        )
        if not success:
            return success, query, ""

        success, reply_sentence = context.understand_reply(reply)
        if not success:
            return success, query, ""

        if not html_report.save(
            object_name=object_name,
            filename=file.add_extension(filename, "html"),
        ):
            return False, query, ""

        logger.info(
            "query: {}, reply: {}".format(
                string.pretty_bytes(len(query)),
                string.pretty_bytes(len(reply_sentence)),
            )
        )

        if not loop:
            break

    return True, query, reply_sentence
