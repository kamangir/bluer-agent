from flask import request, redirect, url_for
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import List_of_Projects
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/save")
def save(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/save: step={step_id}, index={index}")

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Project.load(object_name)
        convo.subject = (request.args.get("subject") or "").strip()
        if not convo.save():
            flash(messages.cannot_save_project)

    lock = FileLock("/tmp/assistant/list_of_projects.lock")
    with lock:
        if not (
            List_of_Projects()
            .update(
                object_name,
                convo.subject,
            )
            .save()
        ):
            flash(messages.cannot_save_list_of_projects)

    return redirect(
        url_for(
            "open_project",
            object_name=object_name,
            index=index,
            step=step_id,
        ),
    )
