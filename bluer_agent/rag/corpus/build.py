from tqdm import tqdm

from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects import objects
from bluer_objects.file import list_of
from bluer_objects.file import name as file_name

from bluer_agent import NAME
from bluer_agent.crawl import file
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def build(
    crawl_object_name: str,
    corpus_object_name: str,
) -> bool:
    logger.info(f"{NAME}.build: {crawl_object_name} -> {corpus_object_name}")

    list_of_filenames = list_of(
        objects.path_of(
            object_name=crawl_object_name,
            filename="*.pkl.gz",
        )
    )
    log_list(
        logger,
        "processing",
        [file_name(filename) for filename in list_of_filenames],
        "file(s)",
    )

    for filename in tqdm(list_of_filenames):
        logger.info("processing {} ...".format(file_name(filename)))

        success, crawl = file.load(filename)
        if not success:
            return success

        for key, text in tqdm(crawl.items()):
            logger.info(
                "processing {}/{} ...".format(
                    file_name(filename),
                    key,
                ),
            )
            logger.info("🪄")

    return True
