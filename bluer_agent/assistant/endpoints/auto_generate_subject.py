from flask import redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash


@app.get("/<object_name>/auto_generate_subject")
def auto_generate_subject(object_name: str):
    convo = Conversation.load(object_name)

    if not convo.generate_subject():
        flash(messages.cannot_generate_subject, "warning")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
