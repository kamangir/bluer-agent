import time
from typing import Tuple

from blueness import module
from bluer_options import string
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.metadata import post_to_object
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent.assets.path import get_path
from bluer_agent.audio.play import play
from bluer_agent.audio.properties import AudioProperties
from bluer_agent.chat.functions import chat
from bluer_agent.chat.messages import List_of_Messages
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
    loop: bool = True,
    post_metadata: bool = True,
    verbose: bool = False,
) -> Tuple[bool, List_of_Messages]:
    logger.info(
        "{}.converse:context[{}] -{}{}> {}".format(
            NAME,
            context.object_name,
            "loop-" if loop else "",
            "metadata-" if post_metadata else "",
            object_name,
        )
    )

    audio_prompt: str = greeting

    list_of_messages = List_of_Messages()

    success: bool = True
    while True:
        html_report = HTMLReport(template=get_path("./query.html"))

        success, filename = generate_voice(
            object_name=object_name,
            sentence=audio_prompt,
        )
        if not success:
            break

        if not play(
            object_name=object_name,
            filename=filename,
        ):
            success = False
            break

        time.sleep(0.1)

        file.delete(
            objects.path_of(
                object_name=object_name,
                filename=filename,
            ),
            log=verbose,
        )

        time.sleep(0.9)

        filename = "{}.wav".format(string.timestamp())

        success, query = transcribe(
            object_name=object_name,
            filename=filename,
            language=language,
            record=True,
            properties=audio_properties,
        )
        if not success or not query:
            break

        success, query_context = context.generate(
            query=query,
            html_report=html_report,
        )
        if not success:
            break

        success, reply = chat(
            messages=build_prompt(
                query=query,
                context=query_context["chunks"],
                previous_messages=list_of_messages,
            ),
            html_report=html_report,
        )
        if not success:
            break

        success, reply_sentence = context.understand_reply(reply)
        if not success:
            break

        list_of_messages.messages.append(
            {
                "role": "assistant",
                "content": reply_sentence,
            }
        )

        if not html_report.save(
            object_name=object_name,
            filename=file.add_extension(filename, "html"),
        ):
            success = False
            break

        logger.info(
            "query: {}, reply: {}".format(
                string.pretty_bytes(len(query)),
                string.pretty_bytes(len(reply_sentence)),
            )
        )

        audio_prompt = reply_sentence

        if not loop:
            break

    if not post_to_object(
        object_name,
        "conversation",
        list_of_messages.messages,
    ):
        success = False

    return success, list_of_messages
