from __future__ import annotations

from dataclasses import dataclass
from rq.job import Job as rq_Job


@dataclass(frozen=True)
class Job:
    job: rq_Job
    task_name: str
    object_name: str
