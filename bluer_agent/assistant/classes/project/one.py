from __future__ import annotations

from typing import Any, List, Tuple, Union, Dict
from dataclasses import dataclass

from bluer_objects import file
from bluer_objects import objects
from bluer_objects.mlflow.tags import set_tags

from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.classes.requirement import Requirement, Step
from bluer_agent.assistant.classes.project import get
from bluer_agent.assistant.functions.chat import chat
from bluer_agent.logger import logger


@dataclass
class GuiElements:
    index_display: str = " - "
    can_delete: bool = False
    can_next: bool = False
    can_prev: bool = False
    can_up: bool = False


TAG = "bluer_agent_assistant_project"


class Project:
    def __init__(self):
        self.object_name: str = ""

        self.list_of_requirements: List[Requirement] = []

        self.subject: str = ""

        self.metadata: Dict[str, Any] = {}

    def generate_subject(self) -> Tuple[bool, str]:
        if not self.list_of_requirements:
            return False, ""

        prompt = """
This is the first objective for the first requirement for building something.
Generate a title for this effort in the same language of the objective. Do not use 
markdown symbols in the title. Do not start the title with "title:"

objective: {}
"""

        success, subject = chat(
            messages=[
                {
                    "role": "user",
                    "content": prompt.format(
                        self.list_of_requirements[0].objective,
                    ),
                }
            ],
            object_name=self.object_name,
        )
        if not success:
            return success, ""

        return True, subject

    def get_context(
        self,
        step_id: str,
    ) -> List[Dict]:
        return Project.get_context_(
            owner=self,
            step_id=step_id,
        )

    @classmethod
    def get_context_(
        cls,
        owner: Union["Project", Step],
        step_id: str,
    ) -> List[Dict]:
        if step_id == "top":
            return []

        for requirement in owner.list_of_requirements:
            step_index = requirement.index_of(step_id)
            if step_index == -1:
                continue

            step = requirement.list_of_steps[step_index]
            assert isinstance(step, Step)

            list_of_messages = [
                {
                    "role": "user",
                    "content": requirement.objective,
                },
                {
                    "role": "assistant",
                    "content": step.content,
                },
            ]

            if step.id == step_id:
                return list_of_messages

            return list_of_messages + cls.get_context_(
                owner=step,
                step_id=step_id,
            )

    def get_gui_elements(
        self,
        index: int,
        step_id: str,
    ) -> Tuple[Any, GuiElements]:
        logger.info(f"generating gui elements for step={step_id}, index={index}")

        list_of_requirements = self.get_list_of_requirements(
            step_id=step_id,
        )

        gui_elements = GuiElements()

        gui_elements.can_up = step_id != "top"

        if len(list_of_requirements) == 0:
            logger.warning(f"requirement not found: step={step_id}, index={index}")
            return None, gui_elements

        gui_elements.can_delete = True

        index = max(min(index, len(list_of_requirements)), 1)

        requirement = (
            list_of_requirements[index - 1]
            if 1 <= index <= len(list_of_requirements)
            else None
        )

        gui_elements.can_prev = index > 1

        gui_elements.can_next = 1 <= index < len(list_of_requirements)

        gui_elements.index_display = f"{index} / {len(list_of_requirements)}"

        return requirement, gui_elements

    def get_requirement(
        self,
        step_id: str = "top",
    ) -> Union[Requirement, Project, None]:
        if step_id == "top":
            return None

        return get.get_requirement(
            step_id=step_id,
            list_of_requirements=self.list_of_requirements,
        )

    def get_list_of_requirements(
        self,
        step_id: str = "top",
    ) -> List[Requirement]:
        return get.get_list_of_requirements(
            step_id=step_id,
            list_of_requirements=self.list_of_requirements,
        )

    def get_owner(
        self,
        step_id: str,
    ) -> Union[Project, Step, None]:
        if step_id == "top":
            return self

        return self.get_step(
            step_id=step_id,
        )

    def get_step(
        self,
        step_id: str = "top",
    ) -> Union[Step, None]:
        return get.get_step(
            step_id=step_id,
            list_of_requirements=self.list_of_requirements,
        )

    def get_top_step_id(
        self,
        step_id: str,
    ) -> str:
        return get.get_top_step_id(
            step_id=step_id,
            list_of_requirements=self.list_of_requirements,
            top_step_id="top",
        )

    @property
    def icon(self) -> str:
        return "({})".format(
            "".join([requirement.icon for requirement in self.list_of_requirements])
        )

    @staticmethod
    def load(
        object_name: str,
    ) -> "Project":
        filename = objects.path_of(
            object_name=object_name,
            filename="project.dat",
        )

        success, convo = file.load(
            filename,
            ignore_error=True,
            default=Project(),
        )

        assert isinstance(convo, Project)
        convo.object_name = object_name

        if not success:
            return convo

        if not isinstance(convo, Project):
            logger.error(
                "Project expected, received {}.".format(
                    convo.__class__.__name__,
                )
            )
            return Project()

        if not convo.migrate():
            return Project()

        logger.info(
            "{}: {} requirement(s) loaded from {}".format(
                convo.__class__.__name__,
                len(convo.list_of_requirements),
                convo.object_name,
            )
        )

        return convo

    def migrate(self) -> bool:
        if not hasattr(self, "metadata"):
            logger.info(f"{self.__class__.__name__}.migrate: += metadata")
            self.metadata = {}

        return True

    def save(self) -> bool:
        filename = objects.path_of(
            object_name=self.object_name,
            filename="project.dat",
        )

        tagged_log: str = ""
        if not self.metadata.get("tagged", False):
            if not set_tags(
                object_name=self.object_name,
                tags=TAG,
                verbose=verbose,
            ):
                return False

            self.metadata["tagged"] = True
            tagged_log = " and tagged"

        if not file.save(
            filename,
            self,
            log=verbose,
        ):
            return False

        logger.info(
            "{}: {} requirement(s) saved to {}{}".format(
                self.__class__.__name__,
                len(self.list_of_requirements),
                self.object_name,
                tagged_log,
            )
        )

        return True
