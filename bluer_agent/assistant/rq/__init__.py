from __future__ import annotations

import os
from redis import Redis
from rq import Queue


REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379/0",
)
redis_conn = Redis.from_url(REDIS_URL)

job_queue = Queue(
    "assistant",
    connection=redis_conn,
    default_timeout=600,  # seconds
)
