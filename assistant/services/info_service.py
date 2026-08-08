"""
=========================================
AMNA AI Assistant
Information Service
=========================================
"""

from datetime import datetime


class InfoService:

    # ==========================================
    # Identity
    # ==========================================

    def who_are_you(self):

        return "I am AMNA, your personal AI assistant."

    def who_created_you(self):

        return "I was created by Amit Yadav."

    def who_is_your_owner(self):

        return "My owner is Amit Yadav."

    def tell_about_amna(self):

        return (
            "I am AMNA, a personal AI assistant designed "
            "to help with conversations, tasks, information, "
            "automation, memory, and everyday activities."
        )

    # ==========================================
    # Time
    # ==========================================

    def get_time(self):

        return datetime.now().strftime("%I:%M %p")

    # ==========================================
    # Date
    # ==========================================

    def get_date(self):

        return datetime.now().strftime("%d %B %Y")