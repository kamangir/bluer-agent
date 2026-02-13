from flask import request, session

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import (
    Conversation,
    List_of_Conversations,
)
from bluer_agent.logger import logger


@app.get("/<object_name>")
def open_conversation(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    logger.info(f"/open: reply={reply_id}, index={index}")

    return List_of_Conversations().render(
        convo=Conversation.load(object_name),
        index=index,
        reply_id=reply_id,
    )
