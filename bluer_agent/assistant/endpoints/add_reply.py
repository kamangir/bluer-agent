from typing import Union
from flask import url_for, request
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.classes.interaction import Interaction, Reply
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/add_reply")
def add_reply(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    logger.info(f"/add_reply on reply={reply_id}, index={index}")

    def redirect(
        index: int = index,
        reply_id: str = reply_id,
    ):
        return flask_redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            )
        )

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Conversation.load(object_name)

        owner = convo.get_owner(reply_id=reply_id)
        if not owner:
            flash(messages.cannot_find_reply)
            return redirect()

        try:
            interaction: Interaction = owner.list_of_interactions[index - 1]
        except Exception as e:
            flash(messages.cannot_find_interaction.format(reply_id, index, e))
            return redirect()

        interaction.list_of_replies.append(Reply(content="..."))

        if not convo.save():
            flash(messages.cannot_save_conversation)

    return redirect()
