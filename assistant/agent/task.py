"""
=========================================
AMNA AI Assistant
Agent Task Models
=========================================
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Task:
    id: int
    description: str
    tool: str
    parameters: Dict = field(default_factory=dict)
    status: str = "pending"


@dataclass
class Plan:
    goal: str
    tasks: List[Task] = field(default_factory=list)
    current: int = 0

    def add_task(self, task: Task):
        self.tasks.append(task)

    def next_task(self):
        if self.current >= len(self.tasks):
            return None

        task = self.tasks[self.current]
        self.current += 1
        return task

    def is_finished(self):
        return self.current >= len(self.tasks)

    def reset(self):
        self.current = 0
        for task in self.tasks:
            task.status = "pending"