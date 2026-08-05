"""
=========================================
AMNA AI Assistant
Router
=========================================
"""

from assistant.intents.memory_intents import MemoryIntent
from assistant.intents.system_intents import SystemIntent
from assistant.intents.search_intents import SearchIntent
from assistant.intents.info_intents import InfoIntent
from assistant.intents.ai_intents import AIIntent


memory_intent = MemoryIntent()
system_intent = SystemIntent()
search_intent = SearchIntent()
info_intent = InfoIntent()
ai_intent = AIIntent()


def route(user, context=None):
    """
    Routes the user request to the appropriate intent.

    Parameters:
        user (str): User message
        context (dict): Conversation context

    Returns:
        str: Assistant response
    """

    command = user.lower().strip()

    # ==========================================
    # Memory Intent
    # ==========================================

    response = memory_intent.handle(command, user)

    if response is not None:
        return response

    # ==========================================
    # System Intent
    # ==========================================

    response = system_intent.handle(command)

    if response is not None:
        return response

    # ==========================================
    # Search Intent
    # ==========================================

    response = search_intent.handle(command, user)

    if response is not None:
        return response

    # ==========================================
    # Information Intent
    # ==========================================

    response = info_intent.handle(command)

    if response is not None:
        return response

    # ==========================================
    # AI Intent (Fallback)
    # ==========================================

    return ai_intent.handle(
        user=user,
        context=context
    )