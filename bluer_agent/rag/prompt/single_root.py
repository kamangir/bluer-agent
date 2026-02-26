from __future__ import annotations
from typing import Dict, List

from blueness import module
from bluer_options import string

from bluer_agent import NAME
from bluer_agent.chat.messages import List_of_Messages
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def build_prompt(
    query: str,
    context: List[Dict],
    top_n: int = 12,
    max_chars_per_hit: int = 420,
    previous_messages: List_of_Messages = List_of_Messages(),
) -> List[Dict]:
    context = sorted(
        context,
        key=lambda x: float(
            x.get("score", 0.0),
        ),
        reverse=True,
    )[:top_n]

    def fmt(hit: Dict) -> str:
        text = (hit.get("text") or "").strip().replace("\n", " ")
        text = text[:max_chars_per_hit]
        return text

    evidence = "\n\n".join(fmt(hit) for i, hit in enumerate(context))

    content = "\n".join(
        [
            "با توجه به شواهد زیر به سوالی که در ادامه آمده است جواب بده. ",
            "اگر شواهد کافی یا مرتبط نیست، بگو «اطلاعات کافی نیست».",
            "",
            "شواهد:",
            evidence,
            "",
            "سوال:",
            query,
            "",
        ]
    )

    logger.info(
        "{}.build_prompt({} query, {} context, top {}): {} + {} previous message(s)".format(
            NAME,
            string.pretty_bytes(len(query)),
            len(context),
            top_n,
            string.pretty_bytes(len(content)),
            len(previous_messages.messages),
        )
    )

    message = {
        "role": "user",
        "content": content,
    }

    previous_messages.messages.append(message)

    return previous_messages.messages
