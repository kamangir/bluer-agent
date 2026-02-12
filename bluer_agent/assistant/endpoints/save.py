from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash


@app.get("/<object_name>/save")
def save(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    convo = Conversation.load(object_name)
    convo.subject = (request.args.get("subject") or "").strip()
    if not convo.save():
        flash(messages.cannot_save_conversation, "warning")

    if not (
        List_of_Conversations()
        .update(
            object_name,
            convo.subject,
        )
        .save()
    ):
        flash(messages.cannot_save_list_of_conversations, "warning")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index,
            reply=reply_id,
        ),
    )
