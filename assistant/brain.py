"""
=========================================
AMNA AI Assistant
Brain
=========================================
"""

from assistant.router import route


def reply(user, context=None):
    """
    Main entry point for AMNA.

    Parameters:
        user (str): User message
        context (dict): Conversation context

    Returns:
        str: Assistant response
    """

    return route(
        user=user,
        context=context
    )