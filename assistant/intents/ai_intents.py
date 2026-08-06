"""
=========================================
AMNA AI Assistant
AI Intent
=========================================
"""

from assistant.ai.llm import ask_llm


class AIIntent:

    def handle(self, user, context=None):
        """
        Handles AI fallback requests.

        Parameters:
            user (str): User message
            context (dict): Conversation context

        Returns:
            str: AI response
        """

        return ask_llm(
            user_message=user,
            context=context
        )