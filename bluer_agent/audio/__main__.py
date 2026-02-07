import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.audio.conversation import converse, greeting
from bluer_agent.audio.play import play
from bluer_agent.audio.record import record
from bluer_agent.audio.properties import AudioProperties
from bluer_agent.rag.corpus.context import Context
from bluer_agent.transcription.functions import list_of_languages
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="converse | play | record",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--context_object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="audio.wav",
)
parser.add_argument(
    "--language",
    type=str,
    default=list_of_languages[0],
    help=" | ".join(list_of_languages),
)
parser.add_argument(
    "--greeting",
    type=str,
    default=greeting,
)
AudioProperties.add_args(parser)

args = parser.parse_args()

audio_properties = AudioProperties(
    channels=args.channels,
    crop_silence=args.crop_silence == 1,
    length=args.length,
    rate=args.rate,
)

success = False
if args.task == "converse":
    success = converse(
        greeting=args.greeting,
        context=Context(args.context_object_name),
        object_name=args.object_name,
        language=args.language,
        audio_properties=audio_properties,
        loop=True,
    )[0]
elif args.task == "play":
    success = play(
        object_name=args.object_name,
        filename=args.filename,
    )
elif args.task == "record":
    success = record(
        object_name=args.object_name,
        filename=args.filename,
        properties=audio_properties,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
