from typing import List, Dict, Tuple, Any
import requests

from blueness import module
from bluer_options.logger.config import log_list

from bluer_agent import NAME
from bluer_agent import env
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def chat(
    messages: List[Dict],
) -> Tuple[bool, Any]:
    log_list(
        logger,
        f"{NAME}.chat({env.BLUER_AGENT_CHAT_MODEL_NAME}):",
        [str(message) for message in messages],
        "message(s)",
    )

    headers = {
        "Authorization": f"apikey {env.BLUER_AGENT_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": env.BLUER_AGENT_CHAT_MODEL_NAME,
        "messages": messages,
        "max_tokens": env.BLUER_AGENT_CHAT_MAX_TOKENS,
        "temperature": env.BLUER_AGENT_CHAT_TEMPERATURE,
    }

    response = requests.post(
        "{}/chat/completions".format(env.BLUER_AGENT_CHAT_ENDPOINT),
        headers=headers,
        json=payload,
        timeout=env.BLUER_AGENT_CHAT_TIMEOUT,
    )

    if response.status_code // 100 != 2:  # Check if status code is not in the 2xx range
        logger.info(
            "failed, status_code: {}, reason: {}.".format(
                response.status_code,
                response.reason,
            )
        )
        return False, ""

    return True, response.json()
