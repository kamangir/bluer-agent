from __future__ import annotations

from blueness import module

from bluer_agent import NAME
from bluer_agent.assistant.classes.project import Project, List_of_Projects

NAME = module.name(__file__, NAME)


def auto_generate_subject(
    convo: Project,
    **kw_args,
) -> bool:
    return List_of_Projects.generate_subject(convo)
