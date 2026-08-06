"""
=========================================
AMNA AI Assistant
Tool Base Class
=========================================
"""

from abc import ABC, abstractmethod


class BaseTool(ABC):

    def __init__(self):

        self.name = self.__class__.__name__

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Every tool must implement execute().
        """
        pass

    def info(self):

        return {
            "name": self.name
        }