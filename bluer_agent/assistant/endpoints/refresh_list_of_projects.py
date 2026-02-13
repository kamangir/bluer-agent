from flask import redirect, url_for
from filelock import FileLock

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import List_of_Projects
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/refresh_list_of_projects")
def refresh_list_of_projects(object_name: str):
    logger.info("/refresh_list_of_projects")

    lock = FileLock("/tmp/assistant/list_of_projects.lock")
    with lock:
        if not List_of_Projects(
            refresh=True,
        ).save():
            flash(messages.cannot_save_list_of_projects)

    return redirect(
        url_for(
            "open_project",
            object_name=object_name,
        )
    )
