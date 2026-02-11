from flask import session

from bluer_agent.assistant.endpoint import app
from bluer_agent.assistant.classes.conversation import Conversation


@app.get("/<object_name>")
def open_conversation(object_name: str):
    if session.get("index", -1) < 0:
        session["index"] = 0

    return Conversation.load(object_name).render()
