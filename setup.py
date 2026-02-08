from blueness.pypi import setup

from bluer_agent import NAME, VERSION, DESCRIPTION, REPO_NAME

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.assets",
        f"{NAME}.assistant",
        f"{NAME}.audio",
        f"{NAME}.chat",
        f"{NAME}.crawl",
        f"{NAME}.help",
        f"{NAME}.rag",
        f"{NAME}.rag.corpus",
        f"{NAME}.rag.prompt",
        f"{NAME}.README",
        f"{NAME}.transcription",
        f"{NAME}.voice",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
            "**/*.html",
        ],
    },
)
