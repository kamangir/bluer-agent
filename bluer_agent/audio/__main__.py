import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.audio.listen import listen
from bluer_agent.audio.play import play
from bluer_agent.audio.record import record
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="listen | play | record",
)
parser.add_argument(
    "--arg",
    type=bool,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "listen":
    success = listen(args.arg)
if args.task == "play":
    success = play(args.arg)
if args.task == "record":
    success = record(args.arg)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
