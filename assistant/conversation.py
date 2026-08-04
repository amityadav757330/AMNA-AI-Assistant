from assistant.services.speech_service import SpeechService
from assistant.services.ai_service import AIService

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

            user = text.lower().strip()

            if user in EXIT_WORDS:

                self.active = False

                self.speech.speak("Goodbye Amit.")

                self.wait_until_done_speaking()

                print("\nConversation Ended.")

                return

            response = self.ai.ask(text)

            print(f"AMNA: {response}")

            self.speech.speak(response)

            self.wait_until_done_speaking()