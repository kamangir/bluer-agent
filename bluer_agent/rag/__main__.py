import argparse
import base64

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.html_report import HTMLReport

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
    "--corpus_object_name",
    type=str,
)
parser.add_argument(
    "--query_object_name",
    type=str,
)
parser.add_argument(
    "--encoded_query",
    type=str,
)
parser.add_argument(
    "--top_k",
    type=int,
    default=5,
)
parser.add_argument(
    "--filename",
    type=str,
    default="query.html",
)
parser.add_argument(
    "--generate_html",
    type=int,
    default=1,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "query":
    html_report = HTMLReport(
        template=(
            file.absolute(
                "../assets/query.html",
                file.path(__file__),
            )
            if args.generate_html == 1
            else ""
        ),
    )

    success, _ = query(
        corpus_object_name=args.corpus_object_name,
        query=base64.b64decode(args.encoded_query).decode("utf-8"),
        top_k=args.top_k,
        html_report=html_report,
    )

    if success:
        success = html_report.save(
            object_name=args.query_object_name,
            filename=args.filename,
        )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
