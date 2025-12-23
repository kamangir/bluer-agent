import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.audio.play import play
from bluer_agent.audio.record import record
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="play | record",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="audio.wav",
)
parser.add_argument(
    "--length",
    type=int,
    default=30,
    help="in seconds",
)
parser.add_argument(
    "--crop_silence",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--rate",
    type=int,
    default=48000,
)
parser.add_argument(
    "--channels",
    type=int,
    default=1,
)
args = parser.parse_args()

success = False
if args.task == "play":
    success = play(
        object_name=args.object_name,
        filename=args.filename,
    )
elif args.task == "record":
    success = record(
        object_name=args.object_name,
        filename=args.filename,
        length=args.length,
        rate=args.rate,
        channels=args.channels,
        crop_silence=args.crop_silence == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
