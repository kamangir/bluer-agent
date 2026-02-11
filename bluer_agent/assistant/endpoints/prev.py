from flask import request, session, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.logger import logger


@app.post("/<object_name>/prev")
def prev(object_name: str):
    index = int(request.args.get("index", 1)) - 1

    if index > 0:
        index -= 1

    logger.info(f"prev -> {index+1}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index + 1,
        )
    )
