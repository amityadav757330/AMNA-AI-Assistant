"""
=========================================
AMNA AI Assistant
Query Planner
=========================================
"""


class QueryPlanner:

    def classify(self, user_message):

        command = user_message.lower().strip()

        # ==========================================
        # Memory
        # ==========================================

        if (
            command.startswith("remember")
            or command.startswith("forget")
            or command.startswith("what is my")
            or command.startswith("my name is")
            or command.startswith("i study at")
            or command.startswith("i live in")
        ):
            return "memory"

        # ==========================================
        # System
        # ==========================================

        if (
            command.startswith("open ")
            or "shutdown" in command
            or "restart" in command
            or "lock pc" in command
            or "cancel shutdown" in command
        ):
            return "system"

        # ==========================================
        # Information
        # IMPORTANT: Must come BEFORE Search
        # ==========================================

        if (
            command in ["time", "date"]
            or "what is the time" in command
            or "what time is it" in command
            or "current time" in command
            or "what is the date" in command
            or "today's date" in command
            or "todays date" in command
            or "current date" in command
            or "ip address" in command
            or "who created you" in command
            or "who are you" in command
            or "who is your owner" in command
            or "tell me about yourself" in command
        ):
            return "info"

        # ==========================================
        # Search
        # ==========================================

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

        # ==========================================
        # Default
        # ==========================================

        return "ai"