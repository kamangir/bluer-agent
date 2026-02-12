from flask import request, session, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.logger import logger


@app.get("/<object_name>/prev")
def prev(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")

    logger.info(f"/prev on reply={reply_id}, index={index}")

    if index > 1:
        index -= 1

    logger.info(f"prev -> reply={reply_id}, index={index}")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
            index=index,
            reply=reply_id,
        )
    )
