from typing import Tuple
from functools import reduce

from blueness import module
from bluer_options import string
from bluer_options.logger.config import shorten_text
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent.rag.corpus.context import Context
from bluer_agent.rag.prompt import build_prompt
from bluer_agent.chat.functions import chat
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def query(
    object_name: str,
    query: str,
    top_k: int = 5,
    html_report: HTMLReport = HTMLReport(),
) -> Tuple[bool, str]:
    logger.info(
        '{}.query[{}]("{}")'.format(
            NAME,
            object_name,
            query,
        )
    )

    context = Context(object_name)

    success, query_context = context.generate(
        query=query,
        top_k=top_k,
    )
    if not success:
        return success, ""

    html_report.replace(
        {
            "query:::": query,
            "model:::": object_name,
            "query_dir:::": "ltr",
            "query_lang:::": "fa",
            "text_dir:::": "ltr",
            "text_lang:::": "fa",
        }
    ).replace(
        {
            "context": reduce(
                lambda x, y: x + y,
                [
                    [
                        "<tr>",
                        '    <td dir="ltr">',
                        '        <a href="{}" target="_blank" rel="noreferrer">{}</a>'.format(
                            chunk["url"],
                            chunk["root"],
                        ),
                        "    </td>",
                        '    <td dir="ltr" class="mono">{}</td>'.format(
                            chunk["chunk_id"]
                        ),
                        '    <td class="mono">{:.2f}</td>'.format(chunk["score"]),
                        # "    <td>",
                        #'        <pre dir="ltr" lang="fa">{}</pre>'.format(
                        #    shorten_text(chunk["text"])
                        # ),
                        # "    </td>",
                        "</tr>",
                        "",
                    ]
                    for chunk in query_context["chunks"]
                ],
                [],
            ),
        },
        contains=True,
    )

    return chat(
        messages=build_prompt(
            query=query,
            context=query_context["chunks"],
        ),
        html_report=html_report,
    )
