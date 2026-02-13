from typing import List
import copy

from bluer_options import string


class Step:
    def __init__(
        self,
        content: str = "",
        list_of_requirements: List["Requirement"] = [],
    ):
        self.id = string.random()

        self.content = content
        self.list_of_requirements = copy.deepcopy(list_of_requirements)

    @property
    def icon(self) -> str:
        return "[{}]".format(
            "".join(requirement.icon for requirement in self.list_of_requirements)
        )


class Requirement:
    def __init__(
        self,
        objective: str = "",
        list_of_steps: List[Step] = [],
    ):
        self.objective = objective
        self.list_of_steps = copy.deepcopy(list_of_steps)

    @property
    def icon(self) -> str:
        return "[{}]".format("".join(step.icon for step in self.list_of_steps))

    def index_of(self, step_id: str) -> int:
        for index, step in enumerate(self.list_of_steps):
            if step.id == step_id:
                return index

            for requirement in step.list_of_requirements:
                if requirement.index_of(step_id) != -1:
                    return index

        return -1
