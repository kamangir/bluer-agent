from bluer_objects import file


def load() -> str:
    success, template_lines = file.load_text(
        file.absolute(
            "../app.html",
            file.path(__file__),
        ),
    )
    if not success:
        return ""

    return "\n".join(template_lines)
