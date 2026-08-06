"""
=========================================
AMNA AI Assistant
Tool Registry
=========================================
"""


class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):

        self.tools[tool.name.lower()] = tool

    def get(self, name):

        return self.tools.get(name.lower())

    def all_tools(self):

        return self.tools