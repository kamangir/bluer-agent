import gzip
import pickle
from typing import Dict, Tuple, List
from functools import reduce

from blueness import module
from bluer_options import string
from bluer_options.logger.config import log_list, shorten_text
from bluer_objects import file, path
from bluer_objects.html_report import HTMLReport
from bluer_objects import objects

from bluer_agent import NAME, ICON
from bluer_agent.host import signature
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)

"""
using gzip-compressed pickle:
    - binary
    - compact
    - easy to load back in Python
"""


def export(
    results: Dict[str, str],
    object_name: str,
    filename: str,
) -> bool:
    filename = file.add_extension(filename, "html")

    if not (
        HTMLReport(
            file.absolute(
                "../assets/review.html",
                file.path(__file__),
            ),
        )
        .replace(
            {
                "title:::": object_name,
                "signature:::": "{} {}".format(
                    ICON,
                    " | ".join(signature()),
                ),
            }
        )
        .replace(
            {
                "content:::": reduce(
                    lambda x, y: x + y,
                    [
                        [
                            "<details>",
                            f'    <summary><a href="{key}">{key}</a></summary>',
                            '    <div class="value">{}</div>'.format(
                                value.replace("\n", " ")
                            ),
                            "</details>",
                        ]
                        for key, value in results.items()
                    ],
                    [],
                ),
            },
            contains=True,
        )
        .save(
            object_name=object_name,
            filename=filename,
        )
    ):
        return False

    full_filename = objects.path_of(
        object_name=object_name,
        filename=filename,
    )

    logger.info(
        "{}.export: {} page(s) -> {} [{}]".format(
            NAME,
            len(results),
            full_filename,
            string.pretty_bytes(file.size(full_filename)),
        )
    )

    return True


def load(
    object_name: str,
    filename: str,
) -> Tuple[bool, Dict[str, str]]:
    full_filename = objects.path_of(
        object_name=object_name,
        filename=filename,
    )

    try:
        with gzip.open(full_filename, "rb") as f:
            payload = pickle.load(f)
    except Exception as e:
        logger.error(e)
        return False, {}

    if (
        not isinstance(payload, dict)
        or payload.get("format") != "site_text_collector"
        or "results" not in payload
    ):
        logger.error("unrecognized binary format.")
        return False, {}

    results = payload["results"]

    log_list(
        logger,
        "loaded from {}/{} [{}]".format(
            object_name,
            filename,
            string.pretty_bytes(file.size(full_filename)),
        ),
        [
            "{}: {}".format(
                key,
                shorten_text(text.replace("\n", " ")),
            )
            for key, text in results.items()
        ],
        "page(s)",
    )

    return True, results


def save(
    results: Dict[str, str],
    object_name: str,
    filename: str,
) -> bool:
    if not results:
        logger.warning("no pages collected; nothing to save.")
        return True

    full_filename = objects.path_of(
        object_name=object_name,
        filename=filename,
    )

    payload = {
        "format": "site_text_collector",
        "version": 1,
        "results": results,
    }
    try:
        with gzip.open(full_filename, "wb") as f:
            pickle.dump(payload, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        logger.error(e)
        return False

    logger.info(
        "{}.save: {} page(s) -> {}/{} [{}]".format(
            NAME,
            len(results),
            object_name,
            filename,
            string.pretty_bytes(file.size(full_filename)),
        )
    )
    return True
