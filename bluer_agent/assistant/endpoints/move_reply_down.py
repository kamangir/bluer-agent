from flask import url_for, request
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/move_reply_down")
def move_reply_down(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    logger.info(f"/move_reply_down on reply={reply_id}, index={index}")

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

        top_reply_id = convo.get_top_reply_id(reply_id=reply_id)
        logger.info(f"top_reply_id: {top_reply_id}")

        interaction = convo.get_top_interaction(reply_id=reply_id)
        if not interaction:
            flash(messages.cannot_find_reply)
            return redirect(reply_id=top_reply_id)

        reply_index = [reply.id for reply in interaction.list_of_replies].index(
            reply_id
        )
        logger.info(f"reply_id={reply_id} -> reply_index={reply_index}")

        if reply_index >= len(interaction.list_of_replies) - 1:
            return redirect(reply_id=top_reply_id)

        try:
            interaction.list_of_replies = (
                interaction.list_of_replies[:reply_index]
                + [interaction.list_of_replies[reply_index + 1]]
                + [interaction.list_of_replies[reply_index]]
                + interaction.list_of_replies[reply_index + 2 :]
            )
        except Exception as e:
            flash(e)
            return redirect(reply_id=top_reply_id)

        if not convo.save():
            flash(messages.cannot_save_conversation)

    return redirect(reply_id=top_reply_id)
