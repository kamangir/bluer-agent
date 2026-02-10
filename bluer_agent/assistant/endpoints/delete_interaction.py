from flask import session, redirect, url_for

from bluer_objects.mlflow import tags
from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.post("/<object_name>/delete_interaction")
def delete_interaction(object_name: str):
    index = session["index"]

    conversation = Conversation(object_name)
    conversation.history.pop(index)
    conversation.save(tag=False)

    logger.info(f"deleted {object_name}/{index}")

    index = min(
        index,
        len(conversation.history) - 1,
    )
    session["index"] = index
    logger.info(f"index: {index}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
