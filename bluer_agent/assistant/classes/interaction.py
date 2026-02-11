from typing import List
import copy


class Reply:
    def __init__(
        self,
        content: str = "",
        list_of_interactions: List["Interaction"] = [],
    ):
        self.content = content
        self.list_of_interactions = copy.deepcopy(list_of_interactions)


class Interaction:
    def __init__(
        self,
        question: str = "",
        list_of_replies: List[Reply] = [],
    ):
        self.question = question
        self.list_of_replies = copy.deepcopy(list_of_replies)
