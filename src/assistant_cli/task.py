from __future__ import annotations

from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
PROJECTS = DATA_DIR / "project.json"


class Project:
    def __init__(self, name: str):
        self.name = name

    @property
    def type(self):
        return self.__class__.__name__.lower()

    def construct_dict(self, id: int):
        return {"name": self.name, "id": id}


class Task(Project):
    def __init__(self, name: str, project_id: int = 0):
        self.name = name
        self.completed = False
        self.project_id = project_id

    def construct_dict(self, id: int):
        return {
            "name": self.name,
            "id": id,
            "project_id": self.project_id,
            "completed": self.completed,
        }
