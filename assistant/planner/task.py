"""
=========================================
AMNA AI Assistant
Task Model
=========================================
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:

    name: str

    task_type: str

    data: dict = field(default_factory=dict)

    completed: bool = False


@dataclass
class Plan:

    tasks: List[Task] = field(default_factory=list)

    current_task: int = 0

    def add(self, task: Task):

        self.tasks.append(task)

    def next_task(self):

        if self.current_task >= len(self.tasks):
            return None

        task = self.tasks[self.current_task]

        self.current_task += 1

        return task

    def finished(self):

        return self.current_task >= len(self.tasks)