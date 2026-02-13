import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.assistant.rq import queue_name
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="get_queue_name",
)
args = parser.parse_args()

success = False
if args.task == "get_queue_name":
    success = True
    print(queue_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
