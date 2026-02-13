from flask import request, session, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.logger import logger


@app.get("/<object_name>/prev")
def prev(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/prev on step={step_id}, index={index}")

    if index > 1:
        index -= 1

    logger.info(f"prev -> step={step_id}, index={index}")

    return redirect(
        url_for(
            "open_project",
            object_name=object_name,
            index=index,
            step=step_id,
        )
    )
