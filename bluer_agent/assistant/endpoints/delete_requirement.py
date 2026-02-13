from typing import Union
from flask import request, url_for
from flask import redirect as flask_redirect
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/delete_requirement")
def delete_requirement(object_name: str):
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

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Project.load(object_name)
        convo.subject = (request.args.get("subject") or "").strip()

        owner = convo.get_owner(step_id=step_id)
        if not owner:
            flash(messages.cannot_find_step.format(step_id))
            return redirect()

        logger.info(
            "/delete_requirement -> step={} -> owner: {}".format(
                step_id,
                owner.__class__.__name__,
            )
        )

        if index < 1 or index > len(owner.list_of_requirements):
            logger.error("bad index={}".format(index))
            return redirect()

        owner.list_of_requirements.pop(index - 1)
        logger.info(f"deleted {object_name}/{step_id}/{index}")

        if not convo.save():
            flash(messages.cannot_save_project)

    index = min(
        index,
        len(owner.list_of_requirements),
    )
    logger.info(f"index: {index}")

    return redirect()
