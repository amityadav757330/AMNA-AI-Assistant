"""
=========================================
AMNA AI Assistant
Router
=========================================
"""

from assistant.planner.query_planner import QueryPlanner

from assistant.intents.memory_intents import MemoryIntent
from assistant.intents.system_intents import SystemIntent
from assistant.intents.search_intents import SearchIntent
from assistant.intents.info_intents import InfoIntent
from assistant.intents.ai_intents import AIIntent


planner = QueryPlanner()

memory_intent = MemoryIntent()
system_intent = SystemIntent()
search_intent = SearchIntent()
info_intent = InfoIntent()
ai_intent = AIIntent()


def route(user, context=None):

    route_type = planner.classify(user)

    # ==========================================
    # Memory
    # ==========================================

    if route_type == "memory":

        return memory_intent.handle(
            command=user.lower().strip(),
            user=user
        )

    # ==========================================
    # System
    # ==========================================

    elif route_type == "system":

        return system_intent.handle(
            command=user.lower().strip()
        )

    # ==========================================
    # Search
    # ==========================================

    elif route_type == "search":

        return search_intent.handle(
            command=user.lower().strip(),
            user=user
        )

    # ==========================================
    # Info
    # ==========================================

    elif route_type == "info":

        return info_intent.handle(
            command=user.lower().strip()
        )

    # ==========================================
    # AI
    # ==========================================

    return ai_intent.handle(
        user=user,
        context=context
    )