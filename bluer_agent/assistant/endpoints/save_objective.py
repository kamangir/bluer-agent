from flask import request, url_for
from flask import redirect as flask_redirect
from filelock import FileLock
from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.post("/<object_name>/save_objective")
def save_objective(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")
    objective = request.form.get("objective")

    def redirect():
        return flask_redirect(
            url_for(
                "open_project",
                object_name=object_name,
                index=index,
                step=step_id,
            ),
        )

    logger.info(
        f"/save_objective: step={step_id}, index={index}, objective={objective}"
    )

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Project.load(object_name)

        requirement = convo.get_requirement(step_id=step_id)
        if not requirement:
            flash(messages.cannot_find_requirement_with_step.format(step_id))
            return redirect()

        requirement.objective = objective

        if not convo.save():
            flash(messages.cannot_save_project)

    return redirect()
