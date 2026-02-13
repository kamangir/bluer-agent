from __future__ import annotations

from blueness import module

from bluer_agent import NAME
from bluer_agent.assistant.classes.project import Project
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.rq.jobs.auto_generate_subject import auto_generate_subject
from bluer_agent.assistant.rq.jobs.submit import submit
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)


def run_job(
    task_name: str,
    object_name: str,
    **kwargs,
) -> bool:
    logger.info(
        "{}.run_job({}): {}".format(
            NAME,
            object_name,
            task_name,
        )
    )

    convo = Project.load(object_name)

    if task_name == "auto_generate_subject":
        auto_generate_subject(convo, **kwargs)
    elif task_name == "submit":
        submit(convo, **kwargs)
    else:
        logger.error(messages.task_not_found.format(task_name))

    return True
