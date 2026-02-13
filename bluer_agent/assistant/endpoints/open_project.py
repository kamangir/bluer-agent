from flask import request, session

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.project import Project, List_of_Projects
from bluer_agent.logger import logger


@app.get("/<object_name>")
def open_project(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")

    logger.info(f"/open_project: step={step_id}, index={index}")

    return List_of_Projects().render(
        convo=Project.load(object_name),
        index=index,
        step_id=step_id,
    )
