from tqdm import tqdm
from typing import List

from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects import objects
from bluer_objects import file as file_

from bluer_agent import NAME
from bluer_agent.crawl import file
from bluer_agent.crawl.functions import url_to_filename
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)


def review(
    object_name: str,
    root: str = "all",
) -> bool:
    logger.info(
        "{}.review({}/{})".format(
            NAME,
            object_name,
            root,
        )
    )

    list_of_filenames: List[str] = [
        file_.name_and_extension(filename)
        for filename in (
            file_.list_of(
                objects.path_of(
                    object_name=object_name,
                    filename="*.pkl.gz",
                )
            )
            if root == "all"
            else [
                objects.path_of(
                    object_name=object_name,
                    filename="{}.pkl.gz".format(url_to_filename(root)),
                )
            ]
        )
    ]

    log_list(
        logger,
        "reviewing",
        list_of_filenames,
        "file(s)",
    )

    for filename in tqdm(list_of_filenames):
        success, results = file.load(
            object_name=object_name,
            filename=filename,
        )
        if not success:
            return success

        success = file.export(
            results=results,
            object_name=object_name,
            filename=filename,
        )
        if not success:
            return success

    return True
