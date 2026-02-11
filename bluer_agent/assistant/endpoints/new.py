from flask import redirect, url_for

from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.classes.conversation import Conversation


@app.post("/<object_name>/new")
def new(object_name: str):
    object_name = objects.unique_object("convo")

    convo = Conversation.load(object_name)
    convo.save()

    List_of_Conversations().append(
        object_name,
        convo.subject,
    ).save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
