from assistant import memory


class MemoryService:

    # =========================
    # Profile
    # =========================

    def get_profile(self):
        return memory.get_profile()

    def save_profile(self, profile):
        memory.save_profile(profile)

    # =========================
    # Preferences
    # =========================

    def get_preferences(self):
        return memory.get_preferences()

    def save_preferences(self, pref):
        memory.save_preferences(pref)

    # =========================
    # Context
    # =========================

    def get_context(self):
        return memory.get_context()

    def save_context(self, context):
        memory.save_context(context)

    def clear_context(self):
        memory.clear_context()

    # =========================
    # Conversation
    # =========================

    def get_conversation(self):
        return memory.get_conversation()

    def save_conversation(self, conversation):
        memory.save_conversation(conversation)

    # =========================
    # Compatibility Methods
    # =========================

    def remember(self, key, value):

        profile = self.get_profile()

        profile[key] = value

        self.save_profile(profile)

        return f"I'll remember your {key} is {value}."

    def recall(self, key):

        profile = self.get_profile()

        return profile.get(key)

    def forget(self, key):

        profile = self.get_profile()

        if key in profile:
            del profile[key]
            self.save_profile(profile)
            return f"I forgot your {key}."

        return f"I don't remember your {key}."

    def show_all_memory(self):

        profile = self.get_profile()

        if not profile:
            return "Your memory is empty."

        result = []

        for k, v in profile.items():
            result.append(f"{k}: {v}")

        return "\n".join(result)

    def clear_all_memory(self):

        self.save_profile({})

        return "Memory cleared."