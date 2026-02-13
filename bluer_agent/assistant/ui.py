from flask import flash as flash_


def flash(
    message: str,
    category: str = "warning",
):
    return flash_(
        (
            f" ⚠️ {message}"
            if category == "warning"
            else f"ℹ️ {message}" if category == "info" else message
        ),
        category,
    )
