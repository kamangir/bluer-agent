from __future__ import annotations

from blueness import module

from bluer_agent import NAME
from bluer_agent.assistant.classes.conversation import (
    Conversation,
    List_of_Conversations,
)

NAME = module.name(__file__, NAME)


def auto_generate_subject(
    convo: Conversation,
    **kw_args,
) -> bool:
    return List_of_Conversations.generate_subject(convo)
