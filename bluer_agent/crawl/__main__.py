import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_objects import objects

from bluer_agent import NAME
from bluer_agent.crawl import file
from bluer_agent.crawl.collect import collect
from bluer_agent.crawl.functions import url_to_filename
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="collect | review",
)
parser.add_argument(
    "--root",
    required=True,
    help='Root URL, e.g. "https://badkoobeh.com/"',
)
parser.add_argument(
    "--page-count",
    type=int,
    default=25,
)
parser.add_argument(
    "--max-depth",
    type=int,
    default=2,
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--out",
    default="site_text.pkl.gz",
)
parser.add_argument(
    "--timeout",
    type=float,
    default=15.0,
)
parser.add_argument(
    "--max-retries",
    type=int,
    default=4,
)
parser.add_argument(
    "--backoff-base",
    type=float,
    default=0.7,
)
parser.add_argument(
    "--backoff-jitter",
    type=float,
    default=0.4,
)
parser.add_argument(
    "--delay",
    type=float,
    default=0.2,
)
args = parser.parse_args()

success = False
if args.task == "collect":
    success = collect(
        root=args.root,
        page_count=args.page_count,
        max_depth=args.max_depth,
        object_name=args.object_name,
        out=args.out,
        timeout=args.timeout,
        max_retries=args.max_retries,
        backoff_base=args.backoff_base,
        backoff_jitter=args.backoff_jitter,
        delay=args.delay,
    )
elif args.task == "review":
    success, _ = file.load(
        objects.path_of(
            object_name=args.object_name,
            filename="{}.pkl.gz".format(url_to_filename(args.root)),
        )
    )
else:
    success = None
sys_exit(logger, NAME, args.task, success)
