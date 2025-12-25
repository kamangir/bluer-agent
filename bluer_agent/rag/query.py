from typing import Tuple
import json

from blueness import module
from bluer_objects import file, objects

from bluer_agent import NAME
from bluer_agent.rag.corpus.context import generate_context
from bluer_agent.rag.prompt import build_prompt
from bluer_agent.chat.functions import chat
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def query(
    object_name: str,
    query: str,
    top_k: int = 5,
) -> Tuple[bool, str]:
    logger.info(f'{NAME}.query[{object_name}]("{query}")')

    success, context = generate_context(
        object_name=object_name,
        query=query,
        top_k=top_k,
    )
    if not success:
        return success, ""

    return chat(
        messages=build_prompt(
            query=query,
            context=context["chunks"],
        )
    )
