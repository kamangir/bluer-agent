from flask import session, request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.chat.functions import chat


@app.post("/<object_name>/submit")
def submit(object_name: str):
    text = (request.form.get("text") or "").strip()

    if not text:
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
            ),
        )

    convo = Conversation(object_name)
    convo.subject = (request.form.get("subject") or "").strip()

    remove_thoughts = bool(request.form.get("remove_thoughts"))

    success, reply = chat(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        remove_thoughts=remove_thoughts,
    )
    assert success

    convo.history.append(
        {
            "input": text,
            "reply": reply,
        }
    )

    index = len(convo.history) - 1

    session["index"] = index

    if index == 0:
        assert convo.generate_subject()
    else:
        assert convo.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
