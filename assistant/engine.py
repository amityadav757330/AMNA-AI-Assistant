from assistant.conversation import Conversation


class AssistantEngine:

    def __init__(self):

        self.conversation = Conversation()

        print("✅ Assistant Engine Initialized")

    def start_conversation(self):

        self.conversation.start()