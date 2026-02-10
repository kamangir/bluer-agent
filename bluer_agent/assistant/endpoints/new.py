from flask import session, redirect, url_for

from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.assistant.classes.conversation import Conversation


@app.post("/<object_name>/new")
def new(object_name: str):
    object_name = objects.unique_object("convo")

    conversation = Conversation(object_name=object_name)
    conversation.save()

    archive = Archive(session["archive"])
    archive.history.append([object_name, conversation.subject])
    archive.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
