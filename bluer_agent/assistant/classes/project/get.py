from typing import List, Union

from bluer_agent.assistant.classes.requirement import Requirement, Step


def get_list_of_requirements(
    step_id: str,
    list_of_requirements: List[Requirement],
) -> List[Requirement]:
    if step_id == "top":
        return list_of_requirements

    for requirement in list_of_requirements:
        for step in requirement.list_of_steps:
            if step.id == step_id:
                return step.list_of_requirements

            output = get_list_of_requirements(
                step_id=step_id,
                list_of_requirements=step.list_of_requirements,
            )
            if output:
                return output

    return []


def get_step(
    step_id: str,
    list_of_requirements: List[Requirement],
) -> Union[Step, None]:
    if step_id == "top":
        return None

    for requirement in list_of_requirements:
        for step in requirement.list_of_steps:
            if step.id == step_id:
                return step

            output = get_step(
                step_id=step_id,
                list_of_requirements=step.list_of_requirements,
            )
            if output:
                return output

    return None


def get_requirement(
    step_id: str,
    list_of_requirements: List[Requirement],
) -> Union[Requirement, None]:
    for requirement in list_of_requirements:
        for step in requirement.list_of_steps:
            if step.id == step_id:
                return requirement

            output = get_requirement(
                step_id=step_id,
                list_of_requirements=step.list_of_requirements,
            )
            if output:
                return output

    return None


def get_top_step_id(
    step_id: str,
    list_of_requirements: List[Requirement],
    top_step_id: str,
) -> str:
    for requirement in list_of_requirements:
        for step in requirement.list_of_steps:
            if step.id == step_id:
                return top_step_id

            output = get_top_step_id(
                step_id=step_id,
                list_of_requirements=step.list_of_requirements,
                top_step_id=step.id,
            )
            if output:
                return output

    return ""
