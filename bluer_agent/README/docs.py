from bluer_objects.README.alias import list_of_aliases

from bluer_agent import NAME
from bluer_agent.README.items import items
from bluer_agent.README import aliases, audio, chat, rag, transcription

docs = (
    [
        {
            "path": "../..",
            "items": items,
            "macros": {
                "aliases:::": list_of_aliases(NAME),
            },
        },
        {
            "path": "../docs",
        },
    ]
    + aliases.docs
    + audio.docs
    + chat.docs
    + rag.docs
    + transcription.docs
)
