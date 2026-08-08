"""
=========================================
AMNA AI Assistant
Information Intent Handler
=========================================
"""

from assistant.services.info_service import InfoService


class InfoIntent:

    def __init__(self):

        self.info = InfoService()

    # ==========================================
    # Handle Information Commands
    # ==========================================

    def handle(self, command):

        if not command:
            return None

        command = command.lower().strip()

        # ==========================================
        # Identity
        # ==========================================

        if command == "who are you":

            return self.info.who_are_you()

        if command == "who created you":

            return self.info.who_created_you()

        if command == "who is your owner":

            return self.info.who_is_your_owner()

        if command == "tell me about yourself":

            return self.info.tell_about_amna()

        # ==========================================
        # Time
        # ==========================================

        if "time" in command:

            return f"The current time is {self.info.get_time()}."

        # ==========================================
        # Date
        # ==========================================

        if "date" in command:

            return f"Today's date is {self.info.get_date()}."

        return None