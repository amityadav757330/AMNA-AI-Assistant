"""
=========================================
AMNA AI Assistant
Tool
=========================================
"""

from assistant.agent.base_tool import BaseTool
from assistant.agent.tool_result import ToolResult


class Tool(BaseTool):

    def __init__(self, name):
        super().__init__(name)

    def execute(self, task, context=None):
        """
        Override this method in child tools.
        """
        return ToolResult.fail(
            f"{self.name} has not implemented execute()."
        )