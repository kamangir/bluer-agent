from flask import url_for, request
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/delete_step")
def delete_step(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/delete_step on step={step_id}, index={index}")

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
        convo.subject = (request.args.get("subject") or "").strip()

        requirement = convo.get_requirement(step_id=step_id)
        if not requirement:
            flash(messages.cannot_find_requirement_with_step.format(step_id))
            return redirect()

        step_index = [step.id for step in requirement.list_of_steps].index(step_id)
        logger.info(f"step_id={step_id} -> step_index={step_index}")

        top_step_id = convo.get_top_step_id(step_id=step_id)
        logger.info(f"top_step_id: {top_step_id}")

        requirement.list_of_steps.pop(step_index)

        if not convo.save():
            flash(messages.cannot_save_project)

    return redirect(
        step_id=top_step_id,
    )
