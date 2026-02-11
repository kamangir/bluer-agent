from flask import session, request, redirect, url_for
import re

from bluer_agent.assistant.endpoints import app
from bluer_agent.assistant.classes.conversation import Conversation
from bluer_agent.assistant.classes.interaction import Interaction, Reply
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.logger import logger


@app.post("/<object_name>/submit")
def submit(object_name: str):
    question = (request.form.get("question") or "").strip()

    selected_item = request.form.get("selected_item", "new-question")
    logger.info(f"selected_item: {selected_item}")

    if not question:
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
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        remove_thoughts=remove_thoughts,
    )

    index = int(request.args.get("index", 1))

    interaction = Interaction(
        question=question,
        list_of_replies=[
            Reply(
                content=reply,
            )
        ],
    )

    if not convo.list_of_interactions:
        convo.list_of_interactions.append(interaction)
        convo.generate_subject()
    else:
        if selected_item == "question":
            convo.list_of_interactions = (
                convo.list_of_interactions[:index]
                + [interaction]
                + convo.list_of_interactions[index:]
            )
        else:  # reply_{reply_index}
            match = re.fullmatch(r"reply_(\d+)", selected_item)
            if not match:
                logger.warning(
                    f"bad selected_item: {selected_item}, expected reply_<reply_index>"
                )
                return redirect(
                    url_for(
                        "open_conversation",
                        object_name=object_name,
                    ),
                )

            reply_index = int(match.group(1))
            logger.info(f"reply_index: {reply_index}")

            selected_interaction = convo.list_of_interactions[index - 1]
            assert isinstance(selected_interaction, Interaction)

            selected_interaction.list_of_replies[
                reply_index
            ].list_of_interactions.append(interaction)

        convo.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
