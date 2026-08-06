"""
=========================================
AMNA AI Assistant
Context Resolver
=========================================
"""


class ContextResolver:

    def __init__(self):

        self.pronouns = {

            "it",
            "he",
            "she",
            "they",
            "them",
            "this",
            "that",
            "these",
            "those"

        }

    def resolve(self, user_message, context):

        if context is None:

            return user_message

        topic = context.get("topic")

        if not topic:

            return user_message

        message = user_message

        words = message.split()

        new_words = []

        replaced = False

        for word in words:

            clean = word.lower().strip(".,?!")

            if clean in self.pronouns and not replaced:

                new_words.append(topic)

                replaced = True

            else:

                new_words.append(word)

        return " ".join(new_words)