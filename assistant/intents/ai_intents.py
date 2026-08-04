from assistant.llm import ask_llm


class AIIntent:

    def handle(self, user):

        return ask_llm(user)