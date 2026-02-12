from flask import flash as flash_


def flash(
    message: str,
    category: str = "message",
):
    return flash_(
        f" ⚠️ {message}" if category == "warning" else message,
        category,
    )
