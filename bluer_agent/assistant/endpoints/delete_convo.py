from flask import redirect, url_for

from bluer_objects.mlflow import tags
from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.logger import logger


@app.post("/<object_name>/delete_convo")
def delete_convo(object_name: str):
    next_object_name: str = ""

    list_of_conversations = List_of_Conversations()
    index: int = list_of_conversations.index(object_name)

    if index == -1:
        logger.warning(f"{object_name} isn't in the list of conversations.")
    else:
        logger.info(f"removed {object_name} (#{index+1})")
        list_of_conversations.contents.pop(index)
        list_of_conversations.save()

        tags.set_tags(
            object_name=object_name,
            tags="~convo",
            verbose=verbose,
        )

        try:
            next_object_name = list_of_conversations.contents[
                min(
                    index,
                    len(list_of_conversations.contents) - 1,
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
            index=index + 1,
        )
    )
