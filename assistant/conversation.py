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

    def start(self):

        if self.active:
            return

        self.active = True

        speak("Hello Amit. I'm listening.")

        while self.active:

            print("\n🎤 Listening...")

            text = listen()

            if not text:
                continue

            user = text.lower().strip()

            if user in EXIT_WORDS:

                speak("Goodbye Amit.")

                while speaking():
                    time.sleep(0.05)

                self.active = False

                break

            response = reply(text)

            speak(response)

            while speaking():
                time.sleep(0.05)

        print("\nConversation Ended.")