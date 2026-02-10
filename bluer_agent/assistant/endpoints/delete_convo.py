from flask import session, redirect, url_for

from bluer_objects.mlflow import tags
from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.logger import logger


@app.post("/<object_name>/delete_convo")
def delete_convo(object_name: str):
    next_object_name: str = ""

    archive = Archive()
    index: int = archive.index()

    if index == -1:
        logger.warning(f"{object_name} isn't in archive.")
    else:
        logger.info(f"removed {object_name}")
        archive.history.pop(index)
        archive.save()

        tags.set_tags(
            object_name=object_name,
            tags="~convo",
            verbose=verbose,
        )

        try:
            next_object_name = archive.history[
                min(
                    index,
                    len(archive.history) - 1,
                )
            ][0]
        except:
            pass

    if not next_object_name:
        next_object_name = objects.unique_object("convo")

    logger.info(f"next_object_name: {next_object_name}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=next_object_name,
        )
    )
