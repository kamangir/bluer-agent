from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.archive import Archive
from bluer_agent.assistant.classes.conversation import Conversation


@app.post("/<object_name>/save")
def save(object_name: str):
    convo = Conversation(object_name)
    convo.subject = (request.form.get("subject") or "").strip()
    assert convo.save(tag=False)

    archive = Archive()
    for pair in archive.history:
        if pair[0] == object_name:
            pair[1] = convo.subject
            break
    assert archive.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
