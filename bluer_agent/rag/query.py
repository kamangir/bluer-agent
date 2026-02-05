from typing import Tuple

from blueness import module
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent.rag.corpus.context import Context
from bluer_agent.rag.prompt import multi_root, single_root
from bluer_agent.chat.functions import chat
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def query(
    corpus_object_name: str,
    query: str,
    top_k: int = 5,
    html_report: HTMLReport = HTMLReport(),
) -> Tuple[bool, str]:
    logger.info(
        '{}.query[{}]("{}")'.format(
            NAME,
            corpus_object_name,
            query,
        )
    )

    context = Context(corpus_object_name)

    success, query_context = context.generate(
        query=query,
        top_k=top_k,
        html_report=html_report,
    )
    if not success:
        return success, ""

    return chat(
        messages=(
            single_root.build_prompt
            if len(context.list_of_roots) == 1
            else multi_root.build_prompt
        )(
            query=query,
            context=query_context["chunks"],
        ),
        html_report=html_report,
    )
