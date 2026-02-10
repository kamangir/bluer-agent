from flask import session, redirect, url_for

from bluer_objects.mlflow import tags
from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.logger import logger


@app.post("/<object_name>/delete")
def delete_convo(object_name: str):
    next_object_name: str = ""
    archive = Archive(session["archive"])

    if object_name not in archive.list_of:
        logger.warning(f"{object_name} isn't in archive.")
    else:
        index = archive.list_of.index(object_name)

        logger.info(f"removed {object_name}")
        archive.list_of = [
            object_name_
            for object_name_ in archive.list_of
            if object_name_ != object_name
        ]
        archive.save()

        tags.set_tags(
            object_name=object_name,
            tags="~convo",
            verbose=verbose,
        )

        try:
            next_object_name = archive.list_of[
                min(
                    index,
                    len(archive.list_of) - 1,
                )
            ]
        except:
            pass

    if not next_object_name:
        next_object_name = objects.unique_object("convo")

    return redirect(
        url_for(
            "open_conversation",
            object_name=next_object_name,
        )
    )
