"""
=========================================
AMNA AI Assistant
Topic Extractor
=========================================
"""

import re


class TopicExtractor:

    def __init__(self):

        self.patterns = [

            r"tell me about (.+)",
            r"what is (.+)",
            r"who is (.+)",
            r"who was (.+)",
            r"explain (.+)",
            r"describe (.+)",
            r"search (.+)",
            r"search for (.+)",
            r"information about (.+)",
            r"learn about (.+)",
        ]

    def extract(self, text):

        text = text.lower().strip()

        for pattern in self.patterns:

            match = re.search(pattern, text)

            if match:

                topic = match.group(1).strip()

                topic = topic.rstrip("?.")

                return topic.title()

        return None