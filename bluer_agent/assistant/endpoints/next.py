from flask import session, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation


@app.post("/<object_name>/next")
def next(object_name: str):
    convo = Conversation.load(object_name)

    if session["index"] < len(convo.list_of_interactions) - 1:
        session["index"] += 1

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
