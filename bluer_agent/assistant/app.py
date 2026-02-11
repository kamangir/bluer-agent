from __future__ import annotations

import argparse

from blueness import module

from bluer_agent import env
from bluer_agent import NAME
from bluer_agent.assistant.endpoints import app
from bluer_agent.logger import logger

# needed, although seem unused :)
from bluer_agent.assistant.endpoints.auto_generate_subject import auto_generate_subject
from bluer_agent.assistant.endpoints.delete_convo import delete_convo
from bluer_agent.assistant.endpoints.delete_interaction import delete_interaction
from bluer_agent.assistant.endpoints.home import home
from bluer_agent.assistant.endpoints.next import next
from bluer_agent.assistant.endpoints.new import new
from bluer_agent.assistant.endpoints.open import open_conversation
from bluer_agent.assistant.endpoints.prev import prev
from bluer_agent.assistant.endpoints.save import save
from bluer_agent.assistant.endpoints.submit import submit
from bluer_agent.assistant.endpoints.up import up

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
