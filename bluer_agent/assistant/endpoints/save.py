from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.classes.conversation import Conversation


@app.get("/<object_name>/save")
def save(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    convo = Conversation.load(object_name)
    convo.subject = (request.args.get("subject") or "").strip()
    convo.save()

    List_of_Conversations().update(
        object_name,
        convo.subject,
    ).save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index,
            reply=reply_id,
        ),
    )
