from typing import Union
from flask import url_for, request
from flask import redirect as flask_redirect

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.classes.interaction import Reply
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/next")
def next(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    def redirect():
        return flask_redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            )
        )

    convo = Conversation.load(object_name)

    owner: Union[Conversation, Reply] = (
        convo
        if reply_id == "top"
        else convo.get_reply(
            reply_id=reply_id,
        )
    )
    if not owner:
        flash(messages.cannot_find_reply)
        return redirect()

    logger.info(
        f"/next on reply={reply_id}, index={index} -> owner={owner.__class__.__name__}"
    )

    if index <= len(owner.list_of_interactions) - 1:
        index += 1

    logger.info(f"next -> reply={reply_id}, index={index}")

    return redirect()
