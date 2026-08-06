"""
=========================================
AMNA AI Assistant
Tool Manager
=========================================
"""

from assistant.tools.registry import ToolRegistry
from assistant.tools.browser.browser_tool import BrowserTool


class ToolManager:

    def __init__(self):

        self.registry = ToolRegistry()

        self.load_tools()

    def load_tools(self):

        self.registry.register(BrowserTool())

    def execute(self, tool_name, *args, **kwargs):

        tool = self.registry.get(tool_name)

        if tool is None:
            return f"Tool '{tool_name}' not found."

        return tool.execute(*args, **kwargs)