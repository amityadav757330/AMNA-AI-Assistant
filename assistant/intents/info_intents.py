from assistant.tools import *


class InfoIntent:

    def handle(self, command):

        command = command.lower().strip()

        # Identity
        if command == "who are you":
            return who_are_you()

        if command == "who created you":
            return who_created_you()

        if command == "who is your owner":
            return who_is_your_owner()

        if command == "tell me about yourself":
            return tell_about_amna()

        # Time
        if "time" in command:
            return f"The current time is {get_time()}."

        # Date
        if "date" in command:
            return f"Today's date is {get_date()}."

        return None