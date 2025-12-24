import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_agent import NAME
from bluer_agent.chat.functions import chat
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="validate",
)
args = parser.parse_args()

success = False
if args.task == "validate":
    success, response = chat(
        messages=[
            {
                "role": "user",
                "content": "چرا آسمان آبی است؟",
            }
        ]
    )

    if success:
        logger.info(response)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
