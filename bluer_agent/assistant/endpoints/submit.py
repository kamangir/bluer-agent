from typing import Union
from flask import session, request, redirect, url_for
import re

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.classes.interaction import Interaction, Reply
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.logger import logger


@app.get("/<object_name>/submit")
def submit(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    question = (request.args.get("question") or "").strip()

    if not question:
        logger.warning("question not found.")
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            ),
        )

    convo = Conversation.load(object_name)
    convo.subject = (request.args.get("subject") or "").strip()

    remove_thoughts = bool(request.args.get("remove_thoughts"))

    success, reply = chat(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        remove_thoughts=remove_thoughts,
    )
    if not success:
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            ),
        )

    owner: Union[Conversation, Reply] = (
        convo
        if reply_id == "top"
        else convo.get_reply(
            reply_id=reply_id,
        )
    )

    logger.info(
        "/submit -> reply={}, index={} - owner: {}".format(
            reply_id,
            index,
            owner.__class__.__name__,
        )
    )

    interaction = Interaction(
        question=question,
        list_of_replies=[
            Reply(
                content=reply,
            )
        ],
    )

    owner.list_of_interactions = owner.list_of_interactions = (
        owner.list_of_interactions[:index]
        + [interaction]
        + owner.list_of_interactions[index:]
    )

    if isinstance(owner, Conversation) and len(convo.list_of_interactions) == 1:
        convo.generate_subject()
    else:
        convo.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index + 1,
            reply=reply_id,
        ),
    )
