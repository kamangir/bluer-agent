from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="bluer-agent/assistant/{{}}",
    volume=2,
)

docs = [
    {
        "path": f"../docs/assistant.md",
        "items": ImageItems(
            {
                image_template.format("screenshot-2026-02-11-01-09-15.png"): "",
            }
        ),
    }
]
