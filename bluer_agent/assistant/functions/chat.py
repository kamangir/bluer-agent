from typing import List, Dict, Tuple

from bluer_options import string
from bluer_objects.html_report import HTMLReport

from bluer_agent.assets.path import get_path
from bluer_agent.chat.functions import chat as chat_
from bluer_agent.host import signature
from bluer_agent.logger import logger


def chat(
    messages: List[Dict],
    object_name: str,
    remove_thoughts: bool = True,
    simulated: bool = False,
    retry: int = 3,
    filename: str = "",
) -> Tuple[bool, str]:
    if not filename:
        filename = "{}.html".format(string.timestamp())

    if simulated:
        return True, messages[0]["content"][::-1]

    for retry_index in range(retry):
        if retry_index:
            logger.info(f"retry #{retry_index+1}")

        html_report = HTMLReport(template=get_path("./query.html")).replace(
            {
                "host_signature:::": " | ".join(signature()),
            }
        )

        success, reply = chat_(
            messages=messages,
            remove_thoughts=remove_thoughts,
            html_report=html_report,
        )

        html_report.save(
            object_name=object_name,
            filename=filename,
        )

        if success:
            return success, reply

    return False, ""
