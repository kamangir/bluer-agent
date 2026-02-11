from flask import session, request, redirect, url_for

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

    index = session["index"]

    if not convo.list_of_interactions:
        convo.list_of_interactions.append(
            Interaction(
                question=question,
                list_of_replies=[
                    Reply(
                        content=reply,
                    )
                ],
            )
        )
    else:
        interaction = convo.list_of_interactions[index]
        assert isinstance(interaction, Interaction)
        interaction.question = question
        interaction.list_of_replies.append(
            Reply(
                content=reply,
            )
        )

    if index == 0:
        convo.generate_subject()
    else:
        convo.save()

    return redirect(
        url_for(
            "open_conversation",
            object_name=object_name,
        ),
    )
