from flask import redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.rq.queue import queue_job


@app.get("/<object_name>/auto_generate_subject")
def auto_generate_subject(object_name: str):
    queue_job(
        task_name="auto_generate_subject",
        object_name=object_name,
    )

    return redirect(
        url_for(
            "open_project",
            object_name=object_name,
        ),
    )
