from flask import url_for
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_objects.mlflow import tags
from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/delete_convo")
def delete_convo(object_name: str):
    def redirect(object_name: str = object_name):
        return flask_redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
            )
        )

    logger.info(f"/delete_convo: object_name={object_name}")

    next_object_name: str = ""

    lock = FileLock("/tmp/assistant/list_of_conversations.lock")
    with lock:
        list_of_conversations = List_of_Conversations()
        index: int = list_of_conversations.index(object_name)
        logger.info(f"index:{index}")

        if index == -1:
            logger.warning(f"{object_name} isn't in the list of conversations.")
            return redirect()

        list_of_conversations.contents.pop(index)
        logger.info(f"removed {object_name} (#{index})")

        if not list_of_conversations.save():
            flash(messages.cannot_save_list_of_conversations)

    if not tags.set_tags(
        object_name=object_name,
        tags="~convo",
        verbose=verbose,
    ):
        flash(messages.cannot_set_tags)

    index = min(
        index,
        len(list_of_conversations.contents) - 1,
    )
    try:
        next_object_name = list_of_conversations.contents[index].object_name
    except:
        pass

    if not next_object_name:
        next_object_name = objects.unique_object("convo")

    logger.info(f"next_object_name: {next_object_name}")

    return redirect(
        object_name=next_object_name,
    )
