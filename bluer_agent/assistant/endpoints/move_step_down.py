from flask import url_for, request
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/move_step_down")
def move_step_down(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/move_step_down on step={step_id}, index={index}")

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

        top_step_id = convo.get_top_step_id(step_id=step_id)
        logger.info(f"top_step_id: {top_step_id}")

        requirement = convo.get_requirement(step_id=step_id)
        if not requirement:
            flash(messages.cannot_find_requirement_with_step.format(step_id))
            return redirect(step_id=top_step_id)

        step_index = [step.id for step in requirement.list_of_steps].index(step_id)
        logger.info(f"step_id={step_id} -> step_index={step_index}")

        if step_index >= len(requirement.list_of_steps) - 1:
            return redirect(step_id=top_step_id)

        try:
            requirement.list_of_steps = (
                requirement.list_of_steps[:step_index]
                + [requirement.list_of_steps[step_index + 1]]
                + [requirement.list_of_steps[step_index]]
                + requirement.list_of_steps[step_index + 2 :]
            )
        except Exception as e:
            flash(e)
            return redirect(step_id=top_step_id)

        if not convo.save():
            flash(messages.cannot_save_project)

    return redirect(step_id=top_step_id)
