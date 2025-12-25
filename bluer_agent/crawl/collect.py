#!/usr/bin/env python3
from typing import Dict
import argparse

from bluer_objects import objects
from bluer_objects.metadata import post_to_object

from bluer_agent.crawl.classes import RetryPolicy
from bluer_agent.crawl.functions import url_to_filename
from bluer_agent.crawl.collector import SiteTextCollector
from bluer_agent.crawl import file
from bluer_agent.logger import logger


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--root", required=True, help='Root URL, e.g. "https://badkoobeh.com/"'
    )
    p.add_argument("--page-count", type=int, default=25)
    p.add_argument("--max-depth", type=int, default=2)
    p.add_argument("--object_name", type=str, default="")
    p.add_argument("--out", default="site_text.pkl.gz")
    p.add_argument("--timeout", type=float, default=15.0)
    p.add_argument("--max-retries", type=int, default=4)
    p.add_argument("--backoff-base", type=float, default=0.7)
    p.add_argument("--backoff-jitter", type=float, default=0.4)
    p.add_argument("--delay", type=float, default=0.2)
    args = p.parse_args()

    retry = RetryPolicy(
        max_retries=args.max_retries,
        timeout_s=args.timeout,
        backoff_base_s=args.backoff_base,
        backoff_jitter_s=args.backoff_jitter,
        delay_between_requests_s=args.delay,
    )

    collector = SiteTextCollector(args.root, retry=retry)

    results: Dict[str, str] = {}
    interrupted = False
    try:
        results = collector.collect(
            page_count=args.page_count, max_depth=args.max_depth
        )
    except KeyboardInterrupt:
        interrupted = True
        logger.warning("Ctrl+C, saving partial results...")

    file.save(
        results,
        (
            objects.path_of(
                object_name=args.object_name,
                filename="{}.pkl.gz".format(url_to_filename(args.root)),
            )
            if args.out == "auto"
            else args.out
        ),
    )

    if args.object_name:
        post_to_object(
            args.object_name,
            "crawl_collect",
            list(results.keys()),
        )

    if interrupted:
        raise SystemExit(130)


if __name__ == "__main__":
    main()
