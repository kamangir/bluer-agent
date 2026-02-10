from flask import session

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation


@app.get("/<object_name>")
def open_conversation(object_name: str):
    return Conversation(object_name).render(
        max(
            0,
            session.get("index", -1),
        ),
    )
