from flask import session, redirect, url_for, request

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.post("/<object_name>/next")
def next(object_name: str):
    index = int(request.args.get("index", 1)) - 1

    convo = Conversation.load(object_name)

    if index < len(convo.list_of_interactions) - 1:
        index += 1

    logger.info(f"next -> {index+1}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index + 1,
        )
    )
