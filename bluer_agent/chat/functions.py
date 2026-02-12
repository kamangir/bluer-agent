from typing import List, Dict, Tuple
import requests
import re
from functools import reduce

from blueness import module
from bluer_options.logger.config import log_list
from bluer_objects.html_report import HTMLReport

from bluer_agent import NAME
from bluer_agent import env
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def chat(
    messages: List[Dict],
    remove_thoughts: bool = True,
    html_report: HTMLReport = HTMLReport(),
) -> Tuple[bool, str]:
    log_list(
        logger,
        "{}.chat({}):".format(
            NAME,
            env.BLUER_AGENT_CHAT_MODEL_NAME,
        ),
        [str(message) for message in messages],
        "message(s)",
        max_count=-1,
    )

    html_report.replace(
        {
            "message_count:::": str(len(messages)),
            "model_name:::": "{} @ temperature={}".format(
                env.BLUER_AGENT_CHAT_MODEL_NAME,
                env.BLUER_AGENT_CHAT_TEMPERATURE,
            ),
        }
    ).replace(
        {
            "messages:::": reduce(
                lambda x, y: x + y,
                [
                    [
                        '<div class="card" style="margin-bottom:12px;">',
                        '    <details class="section">',
                        '        <summary class="header">',
                        '            <div class="header-left">',
                        '                <span class="chev">›</span>',
                        '                <h2 class="mono" style="font-size:14px;">{}</h2>'.format(
                            message["role"],
                        ),
                        "            </div>",
                        f'            <div class="pill mono">#{index+1}</div>',
                        "        </summary>",
                        "",
                        '        <div class="content">',
                        '            <div class="block">',
                        '                <pre dir="rtl" lang="fa">',
                        message["content"],
                        "                </pre>",
                        "            </div>",
                        "        </div>",
                        "    </details>",
                        "</div>",
                    ]
                    for index, message in enumerate(messages)
                ],
                [],
            ),
        },
        contains=True,
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

    try:
        response = requests.post(
            "{}/chat/completions".format(env.BLUER_AGENT_CHAT_ENDPOINT),
            headers=headers,
            json=payload,
            timeout=env.BLUER_AGENT_CHAT_TIMEOUT,
        )
    except Exception as e:
        logger.error(f"failed to send request: {e}")
        return False, ""

    success = True
    response_json = {}
    if response.status_code // 100 != 2:  # Check if status code is not in the 2xx range
        logger.info(
            "failed, status_code: {}, reason: {}.".format(
                response.status_code,
                response.reason,
            )
        )
        success = False
    else:
        try:
            response_json = response.json()
        except Exception as e:
            logger.error(f"failed to parse response to json: {e}, response: {response}")
            success = False

    if success:
        if not isinstance(response_json, dict):
            logger.error("response is not a dict")
            success = False
        elif "choices" not in response_json:
            logger.error("choices not in response")
            success = False
        elif len(response_json["choices"]) == 0:
            logger.error("response.choices is empty")
            success = False
        elif len(response_json["choices"]) > 1:
            logger.warning(
                "{} choice(s), will use the first one.".format(response_json["choices"])
            )
    if not success:
        return success, ""

    text = response_json["choices"][0].get("message", {}).get("content", "")

    html_report.replace(
        {
            "thoughts:::": [text],
        },
        contains=True,
    )

    if remove_thoughts and text:
        text = re.sub(
            r"<think>.*?</think>",
            "",
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )

    text = re.sub(r"\s+", " ", text).strip()

    logger.info(text)

    html_report.replace(
        {
            "reply:::": [text],
        },
        contains=True,
    )

    return success, text
