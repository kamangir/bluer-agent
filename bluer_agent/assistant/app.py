from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List
from flask import Flask, request, session, redirect, url_for, render_template_string

from bluer_objects import file

from bluer_agent import env
from bluer_agent.logger import logger

app = Flask(__name__)
app.secret_key = "change-me"  # required for sessions



PAGE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Mini Flask Chat</title>
  <style>
    body { font-family: system-ui, Arial; max-width: 800px; margin: 24px auto; padding: 0 12px; }
    textarea { width: 100%; height: 110px; font-size: 16px; padding: 10px; }
    .row { display: flex; gap: 8px; align-items: center; margin-top: 10px; }
    button { padding: 10px 14px; font-size: 14px; cursor: pointer; }
    .card { border: 1px solid #ddd; border-radius: 10px; padding: 12px; margin-top: 12px; }
    .muted { color: #666; font-size: 13px; }
    pre { white-space: pre-wrap; word-break: break-word; margin: 8px 0 0; }
  </style>
</head>
<body>
  <h2>Mini Flask App</h2>

  <form method="post" action="{{ url_for('submit') }}">
    <label class="muted">Enter a sentence:</label>
    <textarea name="text" placeholder="Type here..."></textarea>
    <div class="row">
      <button type="submit">Run</button>
      <button type="submit" formaction="{{ url_for('prev') }}" {% if not can_prev %}disabled{% endif %}>Prev</button>
      <button type="submit" formaction="{{ url_for('next') }}" {% if not can_next %}disabled{% endif %}>Next</button>
      <button type="submit" formaction="{{ url_for('clear') }}">Clear</button>
      <span class="muted">Showing {{ idx_display }}</span>
    </div>
  </form>

  {% if item %}
    <div class="card">
      <div class="muted">Input</div>
      <pre>{{ item["input"] }}</pre>
      <div class="muted" style="margin-top:10px;">Reply</div>
      <pre>{{ item["reply"] }}</pre>
    </div>
  {% else %}
    <p class="muted">No interactions yet.</p>
  {% endif %}
</body>
</html>
"""


@dataclass
class Interaction:
    input: str
    reply: str


def process_text(text: str) -> str:
    # TODO: replace this with your real processing
    # Example: reverse + uppercase
    return text[::-1].upper()


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

    return render_template_string(
        PAGE,
        item=item,
        can_prev=can_prev,
        can_next=can_next,
        idx_display=idx_display,
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


@app.post("/clear")
def clear():
    session.pop("history", None)
    session.pop("index", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=env.BLUER_AGENT_ASSISTANT_PORT,
    )
