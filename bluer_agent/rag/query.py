from typing import Tuple
from functools import reduce

from blueness import module
from bluer_objects import objects
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent.host import signature
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
            "context_count:::": str(len(query_context["chunks"])),
            "model:::": object_name,
            "query:::": query,
            "query_dir:::": "ltr",
            "query_lang:::": "fa",
            "signature:::": " | ".join(
                objects.signature(
                    object_name="TBA",
                    info="TBA",
                )
                + signature()
            ),
            "text_dir:::": "ltr",
            "text_lang:::": "fa",
        }
    ).replace(
        {
            "context:::": reduce(
                lambda x, y: x + y,
                [
                    [
                        "<tr>",
                        '    <td dir="ltr">',
                        '        <a href="{}" target="_blank" rel="noreferrer" title="{}">{}#{}</a>'.format(
                            chunk["url"],
                            chunk["text"],
                            chunk["root"],
                            chunk["chunk_id"],
                        ),
                        "    </td>",
                        '    <td class="mono">{:.2f}</td>'.format(chunk["score"]),
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
