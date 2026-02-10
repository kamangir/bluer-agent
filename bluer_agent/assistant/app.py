from __future__ import annotations

import argparse

from flask import Flask, session, request, redirect, url_for

from blueness import module
from bluer_objects import objects

from bluer_agent import env
from bluer_agent import NAME
from bluer_agent.chat.functions import chat
from bluer_agent.assistant.conversation import Conversation
from bluer_agent.logger import logger

APP_NAME = module.name(__file__, NAME)

app = Flask(__name__, static_folder="static")
app.secret_key = "change-me"  # not strictly needed now, but fine to keep


@app.get("/")
def home():
    object_name = app.config.get("object_name", "")
    if not object_name:
        object_name = objects.unique_object("convo")

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )


@app.get("/<object_name>")
def open_conversation(object_name: str):
    if session.get("index", -1) < 0:
        session["index"] = 0

    return Conversation.render(
        object_name,
        session["index"],
    )


@app.post("/<object_name>/submit")
def submit(object_name: str):
    text = (request.form.get("text") or "").strip()

    if not text:
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
            ),
        )

    convo = Conversation.load(object_name)
    convo.subject = (request.form.get("subject") or "").strip()

    remove_thoughts = bool(request.form.get("remove_thoughts"))

    _, reply = chat(
        messages=[{"role": "user", "content": text}],
        remove_thoughts=remove_thoughts,
    )

    convo.history.append(
        [
            {
                "input": text,
                "reply": reply,
            }
        ]
    )

    session["index"] = len(convo.history) - 1

    convo.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )


@app.post("/<object_name>/prev")
def prev(object_name: str):
    if session["index"] > 0:
        session["index"] -= 1

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )


@app.post("/<object_name>/next")
def next(object_name: str):
    convo = Conversation.load(object_name)

    if session["index"] < len(convo.history) - 1:
        session["index"] += 1

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )


@app.post("/<object_name>/new")
def new(object_name: str):
    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        )
    )


# -----------------------------
# Main
# -----------------------------


if __name__ == "__main__":
    parser = argparse.ArgumentParser(APP_NAME)
    parser.add_argument("--port", type=int, default=env.BLUER_AGENT_ASSISTANT_PORT)
    parser.add_argument("--hostname", type=str, default="0.0.0.0")
    parser.add_argument("--object_name", type=str)
    args = parser.parse_args()

    logger.info(
        "{} on host:{}, port:{} -> {}".format(
            APP_NAME,
            args.hostname,
            args.port,
            args.object_name,
        )
    )

    # if provided, home (/) will redirect to this.
    if args.object_name:
        app.config["object_name"] = args.object_name

    app.run(
        debug=True,
        host=args.hostname,
        port=args.port,
    )
