import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent.host import signature
from bluer_agent.assets.path import get_path
from bluer_agent.chat.functions import chat
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="validate",
)
parser.add_argument(
    "--prompt",
    type=str,
    default="چرا آسمان آبی است؟",
)
parser.add_argument(
    "--remove_thoughts",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="report.html",
)
args = parser.parse_args()

success = False
if args.task == "validate":
    html_report = HTMLReport(template=get_path("./query.html")).replace(
        {
            "corpus_name:::": "",
            "host_signature:::": " | ".join(signature()),
            "query:::": args.prompt,
            "title:::": "AI query",
        }
    )

    success, _ = chat(
        messages=[
            {
                "role": "user",
                "content": args.prompt,
            }
        ],
        remove_thoughts=args.remove_thoughts == 1,
        html_report=html_report,
    )

    html_report.save(
        object_name=args.object_name,
        filename=args.filename,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
