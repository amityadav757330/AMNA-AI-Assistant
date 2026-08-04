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


def route(user):

    command = user.lower().strip()

    # Memory
    response = memory_intent.handle(command, user)
    if response is not None:
        return response

    # System
    response = system_intent.handle(command)
    if response is not None:
        return response

    # Search
    response = search_intent.handle(command, user)
    if response is not None:
        return response

    # Info
    response = info_intent.handle(command)
    if response is not None:
        return response

    # AI Fallback
    return ai_intent.handle(user)