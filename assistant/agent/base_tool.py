"""
=========================================
AMNA AI Assistant
Base Tool
=========================================
"""

from abc import ABC, abstractmethod


class BaseTool(ABC):

    def __init__(self, name):

        self.name = name

    @abstractmethod
    def execute(self, task, context=None):
        """
        Execute a task.

        Parameters:
            task: Agent Task
            context: Conversation Context

        Returns:
            Any
        """
        pass