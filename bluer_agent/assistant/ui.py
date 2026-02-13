from flask import flash as flash_

from bluer_agent.logger import logger


def flash(
    message: str,
    category: str = "warning",
):
    icon: str = ""
    if category == "warning":
        logger.warning(message)
        icon = "⚠️ "
    elif category == "info":
        logger.info(message)
        icon = "ℹ️ "
    else:
        logger.info(f"{message} - category: {category}")

    return flash_(
        (f"{icon}{message}"),
        category,
    )
