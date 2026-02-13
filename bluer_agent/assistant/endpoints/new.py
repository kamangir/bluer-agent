from flask import redirect, url_for
from filelock import FileLock

from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash


@app.get("/<object_name>/new")
def new(object_name: str):
    object_name = objects.unique_object("convo")

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Conversation.load(object_name)
        if not convo.save():
            flash(messages.cannot_save_conversation)

    lock = FileLock("/tmp/assistant/list_of_conversations.lock")
    with lock:
        if (
            not List_of_Conversations()
            .append(
                object_name,
                convo.subject,
            )
            .save()
        ):
            flash(messages.cannot_save_list_of_conversations)

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
