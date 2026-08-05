"""
=========================================
AMNA AI Assistant
Memory Service
=========================================
"""

from assistant import memory
from assistant.models.user_profile import UserProfile


class MemoryService:

    # =========================================
    # PROFILE
    # =========================================

    def get_profile(self):

        data = memory.get_profile()

        return UserProfile.from_dict(data)

    def save_profile(self, profile):

        if isinstance(profile, UserProfile):
            memory.save_profile(profile.to_dict())
        else:
            memory.save_profile(profile)

    def update_profile(self, data):

        if not data:
            return

        profile = self.get_profile()

        profile.update(data)

        self.save_profile(profile)

    # =========================================
    # PREFERENCES
    # =========================================

    def get_preferences(self):

        return memory.get_preferences()

    def save_preferences(self, preferences):

        memory.save_preferences(preferences)

    # =========================================
    # CONTEXT
    # =========================================

    def get_context(self):

        return memory.get_context()

    def save_context(self, context):

        memory.save_context(context)

    def clear_context(self):

        memory.clear_context()

    # =========================================
    # CONVERSATION
    # =========================================

    def get_conversation(self):

        return memory.get_conversation()

    def save_conversation(self, conversation):

        memory.save_conversation(conversation)