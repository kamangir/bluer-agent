import os
import requests
from typing import Tuple

from blueness import module
from bluer_objects import objects, file

from bluer_agent import NAME
from bluer_agent import env
from bluer_agent.logger import logger


NAME = module.name(__file__, NAME)


def generate_voice(
    object_name: str,
    sentence: str,
    filename: str = "voice.mp3",
    download: bool = True,
) -> Tuple[bool, str]:
    logger.info(
        '{}.generate_voice: "{}" -{}> {}/{}'.format(
            NAME,
            sentence,
            "downloaded-" if download else "",
            object_name,
            filename,
        )
    )

    full_filename = objects.path_of(
        object_name=object_name,
        filename=filename,
    )

    payload = {
        "text": sentence,
        "speaker": "shahrzad",
        "speed": 1,
        "timestamp": False,
    }

    headers = {
        "gateway-token": env.BLUER_AGENT_VOICE_TOKEN,
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            env.BLUER_AGENT_VOICE_ENDPOINT,
            json=payload,
            headers=headers,
        )
    except Exception as e:
        logger.error(e)
        return False, ""

    # https://chat.openai.com/c/6deb94d0-826a-48de-b5ef-f7d8da416c82
    # response.raise_for_status()
    if response.status_code // 100 != 2:  # Check if status code is not in the 2xx range
        logger.error(
            "status_code: {}, reason: {}.".format(
                response.status_code,
                response.reason,
            )
        )
        return False, ""

    try:
        response_json = response.json()

        url = response_json["data"]["data"]["aiResponse"]["result"]["filename"]
    except Exception as e:
        logger.error(e)
        return False, ""

    return (
        not download
        or file.download(
            url,
            full_filename,
        ),
        full_filename,
    )
