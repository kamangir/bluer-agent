from flask import request, url_for
from flask import redirect as flask_redirect
from filelock import FileLock
from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.post("/<object_name>/save_question")
def save_question(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")
    question = request.form.get("question").replace("\r", "").replace("\n", "")

    def redirect():
        return flask_redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            ),
        )

    logger.info(f"/save_question: reply={reply_id}, index={index}, question={question}")

    lock = FileLock(f"/tmp/assistant/{object_name}.lock")
    with lock:
        convo = Conversation.load(object_name)

        interaction = convo.get_top_interaction(reply_id=reply_id)
        if not interaction:
            flash(messages.cannot_find_interaction)
            return redirect()

        interaction.question = question

        if not convo.save():
            flash(messages.cannot_save_conversation)

    return redirect()
