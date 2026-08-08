from assistant.services.speech_service import SpeechService
from assistant.services.ai_service import AIService
from assistant.services.memory_service import MemoryService
from assistant.core.extractor import Extractor
from assistant.core.context import ContextManager
from assistant.ai.topic_extractor import TopicExtractor

import time


EXIT_WORDS = {
    "bye",
    "goodbye",
    "exit",
    "stop conversation",
    "stop talking",
    "bye amna"
}


WAKE_WORDS = [
    "hey amna",
    "amna"
]


SLEEP_WORDS = [
    "go to sleep",
    "sleep",
    "stop listening",
    "goodbye",
    "bye amna"
]


def contains_wake_word(text):
    if not text:
        return False

    text = text.lower().strip()

    return any(
        text.startswith(word)
        for word in WAKE_WORDS
    )


def remove_wake_word(text):
    text = text.lower().strip()

    for word in WAKE_WORDS:

        if text.startswith(word):
            return text[len(word):].strip()

    return text


def contains_sleep_word(text):
    if not text:
        return False

    text = text.lower().strip()

    return any(
        word in text
        for word in SLEEP_WORDS
    )


class Conversation:

    def __init__(self):

        self.active = False
        self.awake = False

        self.speech = SpeechService()
        self.ai = AIService()
        self.memory = MemoryService()
        self.extractor = Extractor()
        self.context = ContextManager()
        self.topic_extractor = TopicExtractor()

    def wait_until_done_speaking(self):

        while self.speech.speaking():
            time.sleep(0.05)

    def start(self):

        if self.active:
            return

        self.active = True
        self.awake = False

        self.speech.speak("AMNA is ready.")

        self.wait_until_done_speaking()

        while self.active:

            # ==========================================
            # WAIT FOR WAKE WORD
            # ==========================================

            if not self.awake:

                print("\n😴 Waiting for wake word...")

                text = self.speech.listen()

                if not text:
                    continue

                print(f"You: {text}")

                if not contains_wake_word(text):
                    continue

                command = remove_wake_word(text)

                self.awake = True

                # --------------------------------------
                # "Amna" only
                # --------------------------------------

                if not command:

                    self.speech.speak(
                        "Yes Amit, how can I help you?"
                    )

                    self.wait_until_done_speaking()

                    continue

                # --------------------------------------
                # "Amna open google"
                # --------------------------------------

                text = command

            # ==========================================
            # ACTIVE MODE
            # ==========================================

            else:

                print("\n🎤 Listening...")

                text = self.speech.listen()

                if not text:
                    continue

                print(f"You: {text}")

                # Sleep command

                if contains_sleep_word(text):

                    self.speech.speak("Going to sleep.")

                    self.wait_until_done_speaking()

                    self.awake = False

                    continue

            # ==========================================
            # NORMALIZE COMMAND
            # ==========================================

            text = text.lower().strip()

            if not text:
                continue

            print(f"[Command] {text}")

            # ==========================================
            # EXIT
            # ==========================================

            if text in EXIT_WORDS:

                self.active = False
                self.awake = False

                self.context.clear()

                self.speech.speak("Goodbye Amit.")

                self.wait_until_done_speaking()

                print("\nConversation Ended.")

                return

            # ==========================================
            # AUTOMATIC MEMORY LEARNING
            # ==========================================

            facts = self.extractor.extract(text)

            if facts:
                self.memory.update_profile(facts)

            # ==========================================
            # TOPIC EXTRACTION
            # ==========================================

            topic = self.topic_extractor.extract(text)

            if topic:

                self.context.set_topic(topic)

                print(
                    f"[Context] Current Topic -> {topic}"
                )

            # ==========================================
            # BUILD CONTEXT
            # ==========================================

            context = {
                "topic": self.context.get_topic(),
                "last_user": self.context.get_last_user_message(),
                "last_ai": self.context.get_last_ai_response(),
            }

            # ==========================================
            # AI / PLANNER
            # ==========================================

            try:

                response = self.ai.ask(
                    text=text,
                    context=context
                )

            except Exception as e:

                print(
                    f"[Conversation Error] {e}"
                )

                response = (
                    "Sorry Amit, something went wrong."
                )

            # ==========================================
            # UPDATE CONTEXT
            # ==========================================

            self.context.update(
                user_message=text,
                ai_response=response
            )

            # ==========================================
            # RESPONSE
            # ==========================================

            print(f"AMNA: {response}")

            self.speech.speak(response)

            self.wait_until_done_speaking()