from flask import redirect, url_for

from bluer_objects import objects

from bluer_agent.assistant.endpoints import app


@app.get("/")
def home():
    object_name = app.config.get("object_name", "")
    if not object_name:
        object_name = objects.unique_object("convo")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
