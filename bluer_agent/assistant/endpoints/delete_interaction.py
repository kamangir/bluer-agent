from typing import Union
from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.interaction import Reply
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.classes.conversation import get
from bluer_agent.logger import logger


@app.get("/<object_name>/delete_interaction")
def delete_interaction(object_name: str):
    index = int(request.args.get("index", 1)) - 1
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
        "/delete_interaction -> reply={}, index={} - owner: {}".format(
            reply_id,
            index + 1,
            owner.__class__.__name__,
        )
    )

    owner.list_of_interactions.pop(index)
    logger.info(f"deleted {object_name}/{reply_id}/{index+1}")

    convo.save()

    index = min(
        index,
        len(owner.list_of_interactions) - 1,
    )
    logger.info(f"index: {index+1}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index + 1,
            reply=reply_id,
        )
    )
