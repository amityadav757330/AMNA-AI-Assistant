from assistant.speech import listen
from assistant.speak import speak, stop, speaking


class SpeechService:

    def listen(self):
        return listen()

    def speak(self, text):
        speak(text)

    def stop(self):
        stop()

    def speaking(self):
        return speaking()