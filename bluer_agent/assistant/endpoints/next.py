from typing import Union
from flask import url_for, request
from flask import redirect as flask_redirect

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/next")
def next(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    def redirect():
        return flask_redirect(
            url_for(
                "open_project",
                object_name=object_name,
                index=index,
                step=step_id,
            )
        )

    convo = Project.load(object_name)

    owner = convo.get_owner(step_id=step_id)
    if not owner:
        flash(messages.cannot_find_step.format(step_id))
        return redirect()

    logger.info(
        f"/next on step={step_id}, index={index} -> owner={owner.__class__.__name__}"
    )

    if index <= len(owner.list_of_requirements) - 1:
        index += 1

    logger.info(f"next -> step={step_id}, index={index}")

    return redirect()
