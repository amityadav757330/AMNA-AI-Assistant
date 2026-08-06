from assistant.services.speech_service import SpeechService
from assistant.services.ai_service import AIService
from assistant.services.memory_service import MemoryService
from assistant.extractor import Extractor
from assistant.context import ContextManager
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


class Conversation:

    def __init__(self):

        self.active = False

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

        self.speech.speak("Hello Amit. I'm listening.")

        self.wait_until_done_speaking()

        while self.active:

            print("\n🎤 Listening...")

            text = self.speech.listen()

            if not text:
                continue

            print(f"You: {text}")

            # ==========================================
            # Automatic Memory Learning
            # ==========================================

            facts = self.extractor.extract(text)

            if facts:
                self.memory.update_profile(facts)

            # ==========================================
            # Topic Extraction
            # ==========================================

            topic = self.topic_extractor.extract(text)

            if topic:

                self.context.set_topic(topic)

                print(f"[Context] Current Topic -> {topic}")

            user = text.lower().strip()

            # ==========================================
            # Exit
            # ==========================================

            if user in EXIT_WORDS:

                self.active = False

                self.context.clear()

                self.speech.speak("Goodbye Amit.")

                self.wait_until_done_speaking()

                print("\nConversation Ended.")

                return

            # ==========================================
            # Build Context
            # ==========================================

            context = {
                "topic": self.context.get_topic(),
                "last_user": self.context.get_last_user_message(),
                "last_ai": self.context.get_last_ai_response(),
            }

            # ==========================================
            # AI Response
            # ==========================================

            response = self.ai.ask(
                text=text,
                context=context
            )

            # ==========================================
            # Update Conversation Context
            # ==========================================

            self.context.update(
                user_message=text,
                ai_response=response
            )

            print(f"AMNA: {response}")

            self.speech.speak(response)

            self.wait_until_done_speaking()