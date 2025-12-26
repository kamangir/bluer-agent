import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.voice.functions import (
    generate_voice,
    list_of_speakers,
    default_speaker,
)
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="generate",
)
parser.add_argument(
    "--sentence",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--download",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--speaker",
    type=str,
    default=default_speaker,
    help=" | ".join(list_of_speakers),
)
parser.add_argument(
    "--speed",
    type=float,
    default=1.0,
    help=">0",
)
parser.add_argument(
    "--timestamp",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "generate":
    success, _ = generate_voice(
        object_name=args.object_name,
        filename=args.filename,
        sentence=args.sentence,
        download=args.download == 1,
        speaker=args.speaker,
        speed=args.speed,
        timestamp=args.timestamp == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
