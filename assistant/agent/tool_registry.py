"""
=========================================
AMNA AI Assistant
Tool Registry
=========================================
"""

from assistant.intents.memory_intents import MemoryIntent
from assistant.intents.system_intents import SystemIntent
from assistant.intents.search_intents import SearchIntent
from assistant.intents.info_intents import InfoIntent
from assistant.intents.ai_intents import AIIntent


class ToolRegistry:

    def __init__(self):

        self.tools = {

            "memory": MemoryIntent(),

            "system": SystemIntent(),

            "search": SearchIntent(),

            "info": InfoIntent(),

            "ai": AIIntent(),

        }

    def get(self, tool_name):

        return self.tools.get(tool_name)

    def register(self, name, tool):

        self.tools[name] = tool

    def available_tools(self):

        return list(self.tools.keys())