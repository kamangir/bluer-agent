from typing import Union
from flask import request, redirect, url_for

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.classes.interaction import Interaction, Reply
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger


@app.get("/<object_name>/submit")
def submit(object_name: str):
    index = int(request.args.get("index", 1))
    reply_id = request.args.get("reply", "top")
    mode = request.args.get("mode", "ai")

    def return_redirect(index: int = index):
        return redirect(
            url_for(
                "open_conversation",
                object_name=object_name,
                index=index,
                reply=reply_id,
            ),
        )

    question = (request.args.get("question") or "").strip()
    if not question:
        flash(messages.cannot_find_question)
        logger.warning("question not found.")
        return return_redirect()

    convo = Conversation.load(object_name)
    convo.subject = (request.args.get("subject") or "").strip()

    owner: Union[Conversation, Reply] = (
        convo
        if reply_id == "top"
        else convo.get_reply(
            reply_id=reply_id,
        )
    )

    logger.info(
        "/submit -mode={}-> reply={}, index={} - owner: {}".format(
            mode,
            reply_id,
            index,
            owner.__class__.__name__,
        )
    )

    remove_thoughts = bool(request.args.get("remove_thoughts"))

    prompt: str = ""
    prompt_template = """
You are an assistant. Generate an answer to the question given below strictly in the same language of the 
question given below (whether Farsi or English). Separate the answer into {} independent 
sections to help the user digest and use the content. Separate the sections with the 
following mark: --- 

Do not start the sections with \"section:\" or markers like that. Do not use markdown symbols.

question: {{}}
"""
    if mode == "none":
        prompt = "{}"
    elif mode == "ai":
        prompt = prompt_template.format("a maximum of five")
    else:
        prompt = prompt_template.format(mode)

    success, reply = chat(
        messages=convo.get_context(reply_id=reply_id)
        + [
            {
                "role": "user",
                "content": prompt.format(question),
            }
        ],
        object_name=object_name,
        remove_thoughts=remove_thoughts,
    )
    if not success:
        return return_redirect()

    first_interaction = len(owner.list_of_interactions) == 0

    owner.list_of_interactions = owner.list_of_interactions = (
        owner.list_of_interactions[:index]
        + (
            [
                Interaction(
                    question=question,
                    list_of_replies=[
                        Reply(content=reply),
                    ],
                )
            ]
            if mode == "none"
            else [
                Interaction(
                    question=question,
                    list_of_replies=[
                        Reply(content=reply_)
                        for reply_ in [item.strip() for item in reply.split("---")]
                        if reply_
                    ],
                )
            ]
        )
        + owner.list_of_interactions[index:]
    )

    if isinstance(owner, Conversation) and first_interaction:
        if not convo.generate_subject():
            flash(messages.cannot_generate_subject)
            if not convo.save():
                flash(messages.cannot_save_conversation)

    else:
        if not convo.save():
            flash(messages.cannot_save_conversation)

    return return_redirect(index=index + 1)
