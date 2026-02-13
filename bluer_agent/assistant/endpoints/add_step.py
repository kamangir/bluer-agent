from typing import Union
from flask import url_for, request
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.classes.requirement import Requirement, Step
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/add_step")
def add_step(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/add_step on step={step_id}, index={index}")

    def redirect(
        index: int = index,
        step_id: str = step_id,
    ):
        return flask_redirect(
            url_for(
                "open_project",
                object_name=object_name,
                index=index,
                step=step_id,
            )
        )

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Project.load(object_name)

        owner = convo.get_owner(step_id=step_id)
        if not owner:
            flash(messages.cannot_find_step.format(step_id))
            return redirect()

        try:
            requirement: Requirement = owner.list_of_requirements[index - 1]
        except Exception as e:
            flash(messages.cannot_find_requirement.format(step_id, index, e))
            return redirect()

        requirement.list_of_steps.append(Step(content="..."))

        if not convo.save():
            flash(messages.cannot_save_project)

    return redirect()
