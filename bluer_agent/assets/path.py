from bluer_objects import file


def get_path(filename: str) -> str:
    return file.absolute(
        filename,
        file.path(__file__),
    )
