"""
=========================================
AMNA AI Assistant
AI Service
=========================================
"""

from assistant.brain import reply


class AIService:

    def ask(self, user_message, context=None):
        """
        Generate a response from AMNA.

        Parameters:
            user_message (str): Current user input.
            context (dict): Conversation context (optional).

        Returns:
            str: AI response.
        """

        return reply(
            user=user_message,
            context=context
        )