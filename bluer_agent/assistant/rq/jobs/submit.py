from __future__ import annotations

from typing import Union
from filelock import FileLock

from blueness import module

from bluer_agent import NAME
from bluer_agent.assistant.classes.project import Project, List_of_Projects
from bluer_agent.assistant.classes.requirement import Requirement, Step
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.assistant.endpoints import messages
from bluer_agent.assistant.ui import flash
from bluer_agent.logger import logger

NAME = module.name(__file__, NAME)


def submit(
    convo: Project,
    step_id: str,
    index: str,
    mode: str,
    remove_thoughts: bool,
    objective: str,
    **kw_args,
) -> bool:
    logger.info(
        "/submit -mode={}-> step={}, index={}".format(
            mode,
            step_id,
            index,
        )
    )

    prompt: str = ""
    prompt_template = """
You are an assistant. Generate the top {} steps necessary to meet the objective given
below strictly in the same language of the objective given below (whether Farsi 
or English) and separate the steps with the following marker: --- 

Do not start the steps with \"step:\", item numbers, or any other markers. Do not use markdown symbols.

objective: {{}}
"""
    if mode == "none":
        prompt = "{}"
    elif mode == "ai":
        prompt = prompt_template.format("five")
    else:
        prompt = prompt_template.format(mode)

    success, step = chat(
        messages=convo.get_context(step_id=step_id)
        + [
            {
                "role": "user",
                "content": prompt.format(objective),
            }
        ],
        object_name=convo.object_name,
        remove_thoughts=remove_thoughts,
    )
    if not success:
        return success

    lock = FileLock("/tmp/assistant/list_of_projects.lock")
    with lock:
        convo = Project.load(convo.object_name)

        owner = convo.get_owner(step_id=step_id)
        if not owner:
            return False
        logger.info(f"owner: {owner.__class__.__name__}")

        first_requirement = len(owner.list_of_requirements) == 0

        owner.list_of_requirements = owner.list_of_requirements = (
            owner.list_of_requirements[:index]
            + (
                [
                    Requirement(
                        objective=objective,
                        list_of_steps=[
                            Step(content=step),
                        ],
                    )
                ]
                if mode == "none"
                else [
                    Requirement(
                        objective=objective,
                        list_of_steps=[
                            Step(content=step_)
                            for step_ in [item.strip() for item in step.split("---")]
                            if step_
                        ],
                    )
                ]
            )
            + owner.list_of_requirements[index:]
        )

        if not convo.save():
            flash(messages.cannot_save_project)
            return False

    if isinstance(owner, Project) and first_requirement:
        success = List_of_Projects.generate_subject(convo)
        if not success:
            logger.error(messages.cannot_generate_subject)
            return success

    return True
