from __future__ import annotations

from typing import Union
from filelock import FileLock

from blueness import module

from bluer_agent import NAME
from bluer_agent.assistant.classes.conversation import (
    Conversation,
    List_of_Conversations,
)
from bluer_agent.assistant.classes.interaction import Interaction, Reply
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)


def submit(
    convo: Conversation,
    reply_id: str,
    index: str,
    mode: str,
    remove_thoughts: bool,
    question: str,
    **kw_args,
) -> bool:
    logger.info(
        "/submit -mode={}-> reply={}, index={}".format(
            mode,
            reply_id,
            index,
        )
    )

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
        object_name=convo.object_name,
        remove_thoughts=remove_thoughts,
    )
    if not success:
        return success

    lock = FileLock("/tmp/assistant/list_of_conversations.lock")
    with lock:
        convo = Conversation.load(convo.object_name)

        owner: Union[Conversation, Reply] = (
            convo
            if reply_id == "top"
            else convo.get_reply(
                reply_id=reply_id,
            )
        )
        logger.info(f"owner: {owner.__class__.__name__}")

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

        if not convo.save():
            flash(messages.cannot_save_conversation)
            return False

    if isinstance(owner, Conversation) and first_interaction:
        success = List_of_Conversations.generate_subject(convo)
        if not success:
            logger.error(messages.cannot_generate_subject)
            return success

    return True
