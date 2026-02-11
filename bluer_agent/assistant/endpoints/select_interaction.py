from flask import session, request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.logger import logger


@app.post("/<object_name>/select")
def select_interaction(object_name: str):
    selected_item = request.form.get("selected_item", "question")

    logger.info(f"selected item: {selected_item}")

    session["selected_item"] = selected_item
    return redirect(url_for("open_conversation", object_name=object_name))
