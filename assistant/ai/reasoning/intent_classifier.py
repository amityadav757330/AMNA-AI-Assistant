"""
=========================================
AMNA AI Assistant
Intent Classifier
=========================================
"""


class IntentClassifier:

    def classify(self, user_message: str):

        command = user_message.lower().strip()

        # ==========================================
        # Browser
        # ==========================================

        browser_keywords = [
            "open",
            "google",
            "search",
            "youtube",
            "wiki",
            "wikipedia",
            "website"
        ]

        if any(command.startswith(word) for word in browser_keywords):
            return "browser"

        # ==========================================
        # Memory
        # ==========================================

        memory_keywords = [
            "remember",
            "forget",
            "what is my",
            "my name is",
            "i live in",
            "i study at",
            "my favourite",
            "my favorite"
        ]

        if any(command.startswith(word) for word in memory_keywords):
            return "memory"

        # ==========================================
        # System
        # ==========================================

        system_keywords = [
            "shutdown",
            "restart",
            "lock pc",
            "cancel shutdown",
            "open calculator",
            "open notepad",
            "open vscode",
            "open chrome"
        ]

        if any(command.startswith(word) for word in system_keywords):
            return "system"

        # ==========================================
        # Weather
        # ==========================================

        if "weather" in command:
            return "weather"

        # ==========================================
        # Default
        # ==========================================

        return "chat"