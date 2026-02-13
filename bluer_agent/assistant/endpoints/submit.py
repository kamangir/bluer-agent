from flask import request, url_for
from flask import redirect as flask_redirect

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.rq.queue import queue_job
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/submit")
def submit(object_name: str):
    index = int(request.args.get("index", 1))
    step_id = request.args.get("step", "top")
    mode = request.args.get("mode", "ai")

    def redirect(index: int = index):
        return flask_redirect(
            url_for(
                "open_project",
                object_name=object_name,
                index=index,
                step=step_id,
            ),
        )

    objective = (request.args.get("objective") or "").strip()
    if not objective:
        flash(messages.cannot_find_objective)
        logger.warning("objective not found.")
        return redirect()

    queue_job(
        task_name="submit",
        object_name=object_name,
        step_id=step_id,
        index=index,
        mode=mode,
        remove_thoughts=bool(request.args.get("remove_thoughts")),
        objective=objective,
    )

    return redirect(index=index + 1)
