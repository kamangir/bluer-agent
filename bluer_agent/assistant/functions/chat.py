from typing import List, Dict, Tuple

from bluer_agent.chat.functions import chat as chat_

simulated: bool = False


def chat(
    messages: List[Dict],
    remove_thoughts: bool = True,
) -> Tuple[bool, str]:
    if simulated:
        return True, messages[0]["content"][::-1]

    return chat_(
        messages=messages,
        remove_thoughts=remove_thoughts,
    )
