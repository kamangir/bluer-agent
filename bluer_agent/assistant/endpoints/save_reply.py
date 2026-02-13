from flask import request, redirect, url_for
from filelock import FileLock
from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.post("/<object_name>/save_reply")
def save_reply(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")
    reply_content = request.form.get("reply_content")

    logger.info(
        f"/save_reply: reply={reply_id}, index={index}, reply_content={reply_content}"
    )

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Conversation.load(object_name)

        reply = convo.get_reply(reply_id=reply_id)
        if not reply:
            flash(messages.cannot_find_reply)
        else:
            reply.content = reply_content

        if not convo.save():
            flash(messages.cannot_save_conversation)

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index,
            reply=reply_id,
        ),
    )
