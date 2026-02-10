from flask import session, redirect, url_for

from bluer_objects.mlflow import tags
from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.logger import logger


@app.post("/<object_name>/delete_interaction")
def delete_interaction(object_name: str):
    logger.info(
        "🪄 will delete {}/index".format(
            object_name,
        )
    )

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
