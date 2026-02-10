from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from typing import List
from flask import Flask, request, session, redirect, url_for, render_template_string

from blueness import module
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.mlflow.tags import set_tags
from bluer_objects.metadata import post_to_object

from bluer_agent import env
from bluer_agent.host import signature
from bluer_agent import ALIAS, ICON, NAME, VERSION
from bluer_agent.chat.functions import chat
from bluer_agent.logger import logger

verbose: bool = False

NAME = module.name(__file__, NAME)

app = Flask(
    __name__,
    static_folder="static",
)
app.secret_key = "change-me"  # required for sessions


@dataclass
class Interaction:
    input: str
    reply: str


def process_text(text: str) -> str:
    _, reply = chat(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        remove_thoughts=request.form.get("remove_thoughts", type=bool),
    )
    return reply


def _get_history() -> List[dict]:
    return session.get("history", [])


def _set_history(history: List[dict]) -> None:
    session["history"] = history


def _get_index() -> int:
    return int(session.get("index", -1))


def _set_index(i: int) -> None:
    session["index"] = i


@app.get("/")
def index():
    history = _get_history()
    i = _get_index()

    item = history[i] if 0 <= i < len(history) else None
    can_prev = i > 0
    can_next = 0 <= i < len(history) - 1

    if len(history) == 0:
        idx_display = "0 / 0"
    else:
        idx_display = f"{i + 1} / {len(history)}"

    success, template = file.load_text(
        file.absolute(
            "./app.html",
            file.path(__file__),
        )
    )
    if not success:
        return "❗️ app.html not found."

    return render_template_string(
        "\n".join(template),
        item=item,
        can_prev=can_prev,
        can_next=can_next,
        idx_display=idx_display,
        object_name=app.config["object_name"],
        signature=" | ".join(signature()),
        title=f"{ICON} {ALIAS}-{VERSION}",
    )


@app.post("/submit")
def submit():
    text = (request.form.get("text") or "").strip()
    if not text:
        return redirect(url_for("index"))

    reply = process_text(text)

    history = _get_history()
    history.append(asdict(Interaction(input=text, reply=reply)))
    _set_history(history)
    _set_index(len(history) - 1)

    return redirect(url_for("index"))


@app.post("/prev")
def prev():
    i = _get_index()
    if i > 0:
        _set_index(i - 1)
    return redirect(url_for("index"))


@app.post("/next")
def next():
    history = _get_history()
    i = _get_index()
    if 0 <= i < len(history) - 1:
        _set_index(i + 1)
    return redirect(url_for("index"))


@app.post("/new")
def new():
    # save object
    object_name = app.config["object_name"]

    post_to_object(
        object_name=object_name,
        key="convo",
        value={
            "history": session.get("history", []),
        },
    )

    set_tags(
        object_name=object_name,
        tags="convo",
        verbose=verbose,
    )

    # new object
    open_object()

    # clear history
    session.pop("history", None)
    session.pop("index", None)

    return redirect(url_for("index"))


def open_object(object_name: str = ""):
    if not object_name:
        object_name = objects.unique_object("convo")

    app.config["object_name"] = object_name

    logger.info(f"opening {object_name}...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument(
        "--port",
        type=int,
        default=env.BLUER_AGENT_ASSISTANT_PORT,
    )
    parser.add_argument(
        "--hostname",
        type=str,
        default="0.0.0.0",
    )
    parser.add_argument(
        "--object_name",
        type=str,
    )
    args = parser.parse_args()

    logger.info(
        "{} on host:{}, port:{} -> {}".format(
            NAME,
            args.hostname,
            args.port,
            args.object_name,
        )
    )

    open_object(args.object_name)

    app.run(
        debug=True,
        host=args.hostname,
        port=args.port,
    )
