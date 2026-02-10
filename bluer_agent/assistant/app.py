from __future__ import annotations

import argparse

from blueness import module

from bluer_agent import env
from bluer_agent import NAME
from bluer_agent.assistant.suffix import app
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--port",
    type=int,
    default=env.BLUER_AGENT_ASSISTANT_PORT,
)
parser.add_argument(
    "--hostname",
    type=str,
    default="0.0.0.0",
)
parser.add_argument(
    "--object_name",
    type=str,
)
args = parser.parse_args()

logger.info(
    "{} on host:{}, port:{} -> {}".format(
        NAME,
        args.hostname,
        args.port,
        args.object_name,
    )
)

# if provided, home (/) will redirect to this.
if args.object_name:
    app.config["object_name"] = args.object_name

app.run(
    debug=True,
    host=args.hostname,
    port=args.port,
)
