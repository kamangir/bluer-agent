from flask import request, redirect, url_for
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/save")
def save(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    logger.info(f"/save: reply={reply_id}, index={index}")

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Conversation.load(object_name)
        convo.subject = (request.args.get("subject") or "").strip()
        if not convo.save():
            flash(messages.cannot_save_conversation)

    lock = FileLock(f"/tmp/assistant/list_of_conversations.lock")
    with lock:
        if not (
            List_of_Conversations()
            .update(
                object_name,
                convo.subject,
            )
            .save()
        ):
            flash(messages.cannot_save_list_of_conversations)

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index,
            reply=reply_id,
        ),
    )
