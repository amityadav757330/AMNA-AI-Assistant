"""
=========================================
AMNA AI Assistant
Query Planner
=========================================
"""


class QueryPlanner:

    def classify(self, user_message):

        command = user_message.lower().strip()

        # Memory
        if (
            command.startswith("remember")
            or command.startswith("forget")
            or command.startswith("what is my")
            or command.startswith("my name is")
            or command.startswith("i study at")
            or command.startswith("i live in")
        ):
            return "memory"

        # System

        if (
            "open " in command
            or "shutdown" in command
            or "restart" in command
            or "lock pc" in command
            or "cancel shutdown" in command
        ):
            return "system"

        # Search

        if (
            command.startswith("weather")
            or command.startswith("who is")
            or command.startswith("what is")
            or command.startswith("tell me about")
            or command.startswith("google")
            or command.startswith("youtube")
            or command.startswith("search")
        ):
            return "search"

        # Information

        if (
            command == "time"
            or command == "date"
            or "ip address" in command
            or "who created you" in command
            or "who are you" in command
        ):
            return "info"

        # Default

        return "ai"