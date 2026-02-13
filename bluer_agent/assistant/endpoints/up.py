from flask import redirect, url_for, request

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.logger import logger


@app.get("/<object_name>/up")
def up(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/up on step={step_id}, index={index}")

    convo = Project.load(object_name)

    step_id = convo.get_top_step_id(
        step_id=step_id,
    )

    logger.info(f"up -> step={step_id}, index={index}")

    return redirect(
        url_for(
            "open_project",
            object_name=object_name,
            index=index,
            step=step_id,
        )
    )
