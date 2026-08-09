import json
from pathlib import Path

from assistant.models.user_profile import UserProfile


class MemoryService:

    # =========================================
    # INITIALIZATION
    # =========================================

    def __init__(self):

        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)

        self.memory_file = self.data_dir / "memory.json"

        if not self.memory_file.exists():
            self._save_data({
                "profile": {},
                "preferences": {},
                "context": {},
                "conversation": []
            })

    # =========================================
    # INTERNAL FILE METHODS
    # =========================================

    def _load_data(self):

        try:

            with open(
                self.memory_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            return {
                "profile": {},
                "preferences": {},
                "context": {},
                "conversation": []
            }

    def _save_data(self, data):

        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    # =========================================
    # PROFILE
    # =========================================

    def get_profile(self):

        data = self._load_data()

        profile_data = data.get(
            "profile",
            {}
        )

        return UserProfile.from_dict(
            profile_data
        )

    def save_profile(self, profile):

        data = self._load_data()

        if isinstance(profile, UserProfile):

            data["profile"] = profile.to_dict()

        else:

            data["profile"] = profile

        self._save_data(data)

    def update_profile(self, profile_data):

        if not profile_data:
            return

        profile = self.get_profile()

        profile.update(profile_data)

        self.save_profile(profile)

    # =========================================
    # PREFERENCES
    # =========================================

    def get_preferences(self):

        data = self._load_data()

        return data.get(
            "preferences",
            {}
        )

    def save_preferences(self, preferences):

        data = self._load_data()

        data["preferences"] = preferences

        self._save_data(data)

    # =========================================
    # CONTEXT
    # =========================================

    def get_context(self):

        data = self._load_data()

        return data.get(
            "context",
            {}
        )

    def save_context(self, context):

        data = self._load_data()

        data["context"] = context

        self._save_data(data)

    def clear_context(self):

        data = self._load_data()

        data["context"] = {}

        self._save_data(data)

    # =========================================
    # CONVERSATION
    # =========================================

    def get_conversation(self):

        data = self._load_data()

        return data.get(
            "conversation",
            []
        )

    def save_conversation(self, conversation):

        data = self._load_data()

        data["conversation"] = conversation

        self._save_data(data)