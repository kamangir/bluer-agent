import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.rag.query import query
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="query",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--query",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "query":
    success, _ = query(
        object_name=args.object_name,
        query=args.query,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
