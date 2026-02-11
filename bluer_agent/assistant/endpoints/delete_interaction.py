from flask import request, session, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.post("/<object_name>/delete_interaction")
def delete_interaction(object_name: str):
    index = int(request.args.get("index", 1)) - 1

    convo = Conversation.load(object_name)
    convo.list_of_interactions.pop(index)
    convo.save(tag=False)

    logger.info(f"deleted {object_name}/{index+1}")

    index = min(
        index,
        len(convo.list_of_interactions) - 1,
    )
    logger.info(f"index: {index+1}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index + 1,
        )
    )
