from assistant.speech import listen
from assistant.brain import reply
from assistant.speak import speak, speaking

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

    def wait_until_done_speaking(self):
        while speaking():
            time.sleep(0.05)

    def start(self):

        if self.active:
            return

        self.active = True

        speak("Hello Amit. I'm listening.")
        self.wait_until_done_speaking()

        while self.active:

            print("\n🎤 Listening...")

            text = listen()

            if not text:
                continue

            user = text.lower().strip()

            if user in EXIT_WORDS:

                self.active = False

                speak("Goodbye Amit.")
                self.wait_until_done_speaking()

                print("\nConversation Ended.")

                return

            print(f"You: {text}")

            response = reply(text)

            print(f"AMNA: {response}")

            speak(response)
            self.wait_until_done_speaking()