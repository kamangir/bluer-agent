from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.classes.conversation import Conversation


@app.post("/<object_name>/save")
def save(object_name: str):
    convo = Conversation(object_name)
    convo.subject = (request.form.get("subject") or "").strip()
    convo.save(tag=False)

    List_of_Conversations().update(
        object_name,
        convo.subject,
    ).save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
