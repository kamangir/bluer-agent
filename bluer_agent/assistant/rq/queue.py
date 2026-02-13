from __future__ import annotations

from rq.job import Job as rq_Job

from blueness import module

from bluer_agent import NAME
from bluer_agent.assistant.ui import flash
from bluer_agent.assistant.rq.jobs import Job
from bluer_agent.assistant.rq.run import run_job
from bluer_agent.assistant.rq import job_queue
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)


def queue_job(
    task_name: str,
    object_name: str,
    *args,
    **kwargs,
) -> Job:
    job: rq_Job = job_queue.enqueue(
        run_job,
        task_name=task_name,
        object_name=object_name,
        *args,
        **kwargs,
        # retry=3,
    )

    flash(
        "{} -> job queue [{}].".format(
            task_name,
            job.id,
        ),
        "info",
    )

    logger.info(
        "{}.queue.job[{}]: {} -> {}".format(
            NAME,
            object_name,
            task_name,
            job.id,
        )
    )

    return Job(
        job=job,
        task_name=task_name,
        object_name=object_name,
    )
