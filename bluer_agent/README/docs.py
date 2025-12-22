from bluer_agent.README.items import items
from bluer_agent.README import aliases, audio, chat, transcription

docs = (
    [
        {
            "path": "../..",
            "items": items,
        },
        {
            "path": "../docs",
        },
    ]
    + aliases.docs
    + audio.docs
    + chat.docs
    + transcription.docs
)
