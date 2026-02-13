from typing import List
from tqdm import tqdm
from dataclasses import dataclass
from flask import render_template_string
from filelock import FileLock

from bluer_options.logger.config import log_list
from bluer_options.timing import ElapsedTimer
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.mlflow.tags import search

from bluer_agent import env
from bluer_agent import ICON
from bluer_agent.assistant.classes.project import Project, TAG
from bluer_agent.assistant.env import verbose
from bluer_agent.assistant.functions import template
from bluer_agent.host import signature
from bluer_agent.logger import logger


@dataclass
class ProjectSummary:
    object_name: str
    subject: str


class List_of_Projects:
    def __init__(
        self,
        refresh: bool = False,
    ):
        self.filename = objects.path_of(
            object_name=env.BLUER_AGENT_ASSISTANT_CACHE,
            filename="list_of_projects.dat",
        )

        self.contents: List[ProjectSummary] = []

        verb: str = ""
        if not refresh:
            verb = "loaded"
            self.reload()
        if not self.contents:
            verb = "found"
            self.find()

        if verbose:
            log_list(
                logger,
                f"{self.__class__.__name__}: {verb}",
                [project_summary.object_name for project_summary in self.contents],
                "project summary(s)",
            )
        else:
            logger.info(
                "{}: loaded {} project summary(s)".format(
                    self.__class__.__name__,
                    len(self.contents),
                )
            )

        if verb == "found":
            self.save()

    def append(
        self,
        object_name: str,
        subject: str,
    ) -> "List_of_Projects":
        self.contents.append(
            ProjectSummary(
                object_name=object_name,
                subject=subject,
            )
        )

        return self

    def find(self) -> bool:
        self.contents = []

        success, list_of_objects = search(TAG)
        if not success:
            return success

        logger.info("found {} object(s)".format(len(list_of_objects)))

        for object_name in tqdm(list_of_objects):
            convo = Project.load(object_name=object_name)

            self.append(
                object_name,
                convo.subject,
            )

        return True

    @staticmethod
    def generate_subject(
        convo: Project,
    ) -> bool:
        success, subject = convo.generate_subject()
        if not success:
            return success

        lock = FileLock("/tmp/assistant/list_of_projects.lock")
        with lock:
            list_of_projects = List_of_Projects()

            list_of_projects.update(
                convo.object_name,
                subject,
            )

            if not list_of_projects.save():
                return False

        lock = FileLock(f"/tmp/assistant/{convo.object_name}.lock")
        with lock:
            convo = Project.load(convo.object_name)
            convo.subject = subject
            return convo.save()

    def index(self, object_name: str) -> int:
        for index, project_summary in enumerate(self.contents):
            if project_summary.object_name == object_name:
                return index
        return -1

    def reload(self) -> bool:
        self.contents = []

        success, metadata = file.load(
            self.filename,
            ignore_error=True,
            default={},
        )
        if not success:
            return success

        if not isinstance(metadata, dict):
            logger.warning(
                "{}: dict expected, {} received.".format(
                    self.__class__.__name__,
                    metadata.__class__.__name__,
                )
            )
            return False

        self.contents = [
            project_summary
            for project_summary in metadata.get("contents", [])
            if isinstance(project_summary, ProjectSummary)
            and project_summary.object_name
        ]

        return True

    def render(
        self,
        convo: Project,
        index: int,
        step_id: str,
    ) -> str:
        elapsed_timer = ElapsedTimer()

        template_text = template.load()
        if not template_text:
            return "❗️ app.html not found."

        requirement, gui_elements = convo.get_gui_elements(
            index=index,
            step_id=step_id,
        )

        return render_template_string(
            template_text,
            # main view
            requirement=requirement,
            top_requirement=convo.get_requirement(step_id),
            gui_elements=gui_elements,
            index=index,
            object_name=convo.object_name,
            step=convo.get_step(step_id),
            step_id=step_id,
            signature=" | ".join(
                [f"model: {env.BLUER_AGENT_CHAT_MODEL_NAME}"]
                + signature()
                + [
                    "took {}".format(
                        elapsed_timer.as_str(
                            include_ms=True,
                            short=True,
                        ),
                    )
                ]
            ),
            title=f"{ICON} @assistant",
            subject=convo.subject,
            # sidebar
            list_of_projects=self.contents,
            project_count=len(self.contents),
            active_object_name=convo.object_name,
        )

    def save(self) -> bool:
        if verbose:
            log_list(
                logger,
                f"{self.__class__.__name__}: saving",
                [project_summary.object_name for project_summary in self.contents],
                "project(s)",
            )
        else:
            logger.info(
                "{}: saving {} project summary(ies)".format(
                    self.__class__.__name__,
                    len(self.contents),
                )
            )

        return file.save(
            self.filename,
            {
                "contents": self.contents,
            },
            log=True,
        )

    def update(
        self,
        object_name: str,
        subject: str,
    ) -> "List_of_Projects":
        for project_summary in self.contents:
            if project_summary.object_name == object_name:
                project_summary.subject = subject
                break

        return self
