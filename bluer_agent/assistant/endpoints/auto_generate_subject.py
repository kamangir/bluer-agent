from flask import redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation


@app.post("/<object_name>/auto_generate_subject")
def auto_generate_subject(object_name: str):
    convo = Conversation.load(object_name)

    convo.generate_subject()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
