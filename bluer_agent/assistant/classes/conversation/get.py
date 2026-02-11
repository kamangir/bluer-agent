from typing import List, Union

from bluer_agent.assistant.classes.interaction import Interaction, Reply


def get_list_of_interactions(
    reply_id: str,
    list_of_interactions: List[Interaction],
) -> List[Interaction]:
    if reply_id == "top":
        return list_of_interactions

    for interaction in list_of_interactions:
        for reply in interaction.list_of_replies:
            if reply.id == reply_id:
                return reply.list_of_interactions

            output = get_list_of_interactions(
                reply_id=reply_id,
                list_of_interactions=reply.list_of_interactions,
            )
            if output:
                return output

    return []


def get_reply(
    reply_id: str,
    list_of_interactions: List[Interaction],
) -> Union[Reply, None]:
    if reply_id == "top":
        return None

    for interaction in list_of_interactions:
        for reply in interaction.list_of_replies:
            if reply.id == reply_id:
                return reply

            output = get_reply(
                reply_id=reply_id,
                list_of_interactions=reply.list_of_interactions,
            )
            if output:
                return output

    return None


def get_top_interaction(
    reply_id: str,
    list_of_interactions: List[Interaction],
) -> Union[Interaction, None]:
    if reply_id == "top":
        return None

    for interaction in list_of_interactions:
        for reply in interaction.list_of_replies:
            if reply.id == reply_id:
                return interaction

            output = get_top_interaction(
                reply_id=reply_id,
                list_of_interactions=reply.list_of_interactions,
            )
            if output:
                return output

    return None


def get_top_reply_id(
    reply_id: str,
    list_of_interactions: List[Interaction],
    top_reply_id: str,
) -> str:
    for interaction in list_of_interactions:
        for reply in interaction.list_of_replies:
            if reply.id == reply_id:
                return top_reply_id

            output = get_top_reply_id(
                reply_id=reply_id,
                list_of_interactions=reply.list_of_interactions,
                top_reply_id=reply.id,
            )
            if output:
                return output

    return ""
