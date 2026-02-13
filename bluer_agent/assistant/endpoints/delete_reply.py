from flask import redirect, url_for, request

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/delete_reply")
def delete_reply(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    logger.info(f"/delete_reply on reply={reply_id}, index={index}")

    def return_redirect(
        index: int = index,
        reply_id: str = reply_id,
    ):
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            )
        )

    convo = Conversation.load(object_name)
    convo.subject = (request.args.get("subject") or "").strip()

    interaction = convo.get_top_interaction(reply_id=reply_id)
    if not interaction:
        flash(messages.cannot_find_reply)
        return return_redirect()

    reply_index = [reply.id for reply in interaction.list_of_replies].index(reply_id)
    logger.info(f"reply_id={reply_id} -> reply_index={reply_index}")

    top_reply_id = convo.get_top_reply_id(reply_id=reply_id)
    logger.info(f"top_reply_id: {top_reply_id}")

    interaction.list_of_replies.pop(reply_index)

    if not convo.save():
        flash(messages.cannot_save_conversation)

    return return_redirect(
        reply_id=top_reply_id,
    )
