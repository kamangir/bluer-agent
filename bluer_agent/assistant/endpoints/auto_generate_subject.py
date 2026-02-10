from flask import redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.logger import logger


@app.post("/<object_name>/auto_generate_subject")
def auto_generate_subject(object_name: str):
    convo = Conversation(object_name)

    convo.generate_subject()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
