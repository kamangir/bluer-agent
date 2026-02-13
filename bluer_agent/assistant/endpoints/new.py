from flask import redirect, url_for
from filelock import FileLock

from bluer_objects import objects

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import List_of_Projects
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash


@app.get("/<object_name>/new")
def new(object_name: str):
    object_name = objects.unique_object("project")

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Project.load(object_name)
        if not convo.save():
            flash(messages.cannot_save_project)

    lock = FileLock("/tmp/assistant/list_of_projects.lock")
    with lock:
        if (
            not List_of_Projects()
            .append(
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
        )
    )
