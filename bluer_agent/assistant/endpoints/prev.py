from flask import session, redirect, url_for

from bluer_agent.assistant.endpoints import app


@app.post("/<object_name>/prev")
def prev(object_name: str):
    if session["index"] > 0:
        session["index"] -= 1

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
