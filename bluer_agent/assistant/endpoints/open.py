from flask import request, session

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.get("/<object_name>")
def open_conversation(object_name: str):
    index = int(request.args.get("index", 1)) - 1
    reply_id = request.args.get("reply", "top")

    logger.info(f"open: reply={reply_id}, index={index}")

    return Conversation.load(object_name).render(
        index,
        reply_id=reply_id,
    )
