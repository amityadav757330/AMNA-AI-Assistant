"""
=========================================
AMNA AI Assistant
Conversation Context Manager
=========================================
"""


class ContextManager:

    def __init__(self):

        self.topic = None

        self.last_user_message = ""

        self.last_ai_response = ""

    # ==========================================
    # Topic
    # ==========================================

    def set_topic(self, topic):

        self.topic = topic

    def get_topic(self):

        return self.topic

    def clear_topic(self):

        self.topic = None

    # ==========================================
    # Conversation
    # ==========================================

    def update(self, user_message, ai_response):

        self.last_user_message = user_message

        self.last_ai_response = ai_response

    def get_last_user_message(self):

        return self.last_user_message

    def get_last_ai_response(self):

        return self.last_ai_response

    # ==========================================
    # Reset
    # ==========================================

    def clear(self):

        self.topic = None

        self.last_user_message = ""

        self.last_ai_response = ""