from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url


def image_template(suffix):
    return assets_url(
        suffix=f"bluer-agent/assistant/{suffix}",
        volume=2,
        blob=True,
    )


docs = [
    {
        "path": "../docs/assistant.md",
        "items": ImageItems(
            {
                image_template("screenshot-2026-02-13-15-15-06.png"): "",
                image_template("screenshot-2026-02-11-01-09-15.png"): "",
            }
        ),
    }
]
