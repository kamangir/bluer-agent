from typing import Union
from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.interaction import Reply
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/delete_interaction")
def delete_interaction(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    convo = Conversation.load(object_name)
    convo.subject = (request.args.get("subject") or "").strip()

    owner: Union[Conversation, Reply] = (
        convo
        if reply_id == "top"
        else convo.get_reply(
            reply_id=reply_id,
        )
    )

    logger.info(
        "/delete_interaction -> reply={}, index={} -> owner: {}".format(
            reply_id,
            index,
            owner.__class__.__name__,
        )
    )

    if index < 1 or index > len(owner.list_of_interactions):
        logger.error("bad index={}".format(index))
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            )
        )

    owner.list_of_interactions.pop(index - 1)
    logger.info(f"deleted {object_name}/{reply_id}/{index}")

    if not convo.save():
        flash(messages.cannot_save_conversation)

    index = min(
        index,
        len(owner.list_of_interactions),
    )
    logger.info(f"index: {index}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index,
            reply=reply_id,
        )
    )
