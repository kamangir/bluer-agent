from flask import redirect, url_for
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import List_of_Conversations
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/refresh_list_of_conversations")
def refresh_list_of_conversations(object_name: str):
    logger.info("/refresh_list_of_conversations")

    lock = FileLock(f"/tmp/assistant/list_of_conversations.lock")
    with lock:
        if not List_of_Conversations(
            refresh=True,
        ).save():
            flash(messages.cannot_save_list_of_conversations)

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
