from flask import session, redirect, url_for

from bluer_objects import objects

from bluer_agent.assistant.suffix import app


@app.post("/<object_name>/new")
def new(object_name: str):
    object_name = objects.unique_object("convo")
    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )
