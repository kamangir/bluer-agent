from flask import session, redirect, url_for, request

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.get("/<object_name>/up")
def up(object_name: str):
    index = int(request.args.get("index", 1)) - 1
    reply_id = request.args.get("reply", "top")

    logger.info(f"/up on reply={reply_id}, index={index+1}")

    convo = Conversation.load(object_name)

    reply_id = convo.get_top_reply_id(
        reply_id=reply_id,
    )

    logger.info(f"up -> reply={reply_id}, index={index+1}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index + 1,
            reply=reply_id,
        )
    )
