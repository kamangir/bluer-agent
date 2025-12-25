#!/usr/bin/env python3
from typing import Dict
import argparse

from blueness import module
from bluer_objects import objects
from bluer_objects.metadata import post_to_object

from bluer_agent import NAME
from bluer_agent.crawl.classes import RetryPolicy
from bluer_agent.crawl.functions import url_to_filename
from bluer_agent.crawl.collector import SiteTextCollector
from bluer_agent.crawl import file
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def collect(
    root: str,
    page_count: int = 25,
    max_depth: int = 2,
    object_name: str = "",
    out: str = "site_text.pkl.gz",
    timeout: float = 15.0,
    max_retries: int = 4,
    backoff_base: float = 0.7,
    backoff_jitter: float = 0.4,
    delay: float = 0.2,
) -> bool:
    logger.info(f"{NAME}.collect({root})...")

    retry = RetryPolicy(
        max_retries=max_retries,
        timeout_s=timeout,
        backoff_base_s=backoff_base,
        backoff_jitter_s=backoff_jitter,
        delay_between_requests_s=delay,
    )

    collector = SiteTextCollector(root, retry=retry)

    results: Dict[str, str] = {}
    interrupted = False
    try:
        results = collector.collect(
            page_count=page_count,
            max_depth=max_depth,
        )
    except KeyboardInterrupt:
        interrupted = True
        logger.warning("Ctrl+C, saving partial results...")

    if not file.save(
        results,
        (
            objects.path_of(
                object_name=object_name,
                filename="{}.pkl.gz".format(url_to_filename(root)),
            )
            if out == "auto"
            else out
        ),
    ):
        return False

    if object_name and not post_to_object(
        object_name,
        "crawl_collect",
        list(results.keys()),
    ):
        return False

    if interrupted:
        # raise SystemExit(130)
        logger.error("interrupted...")
        return False

    return True
