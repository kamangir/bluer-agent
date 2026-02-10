from flask import session, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.post("/<object_name>/delete")
def delete(object_name: str):
    archive = Archive()

    logger.info("🪄")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
