"""
=========================================
AMNA AI Assistant
Speech Service
=========================================
"""

from assistant.voice.speech import listen
from assistant.voice.speak import speak, stop, speaking


class SpeechService:

    def __init__(self):
        pass

    # ==========================================
    # Listen
    # ==========================================

    def listen(self):
        return listen()

    # ==========================================
    # Speak
    # ==========================================

    def speak(self, text):

        if not text:
            return

        speak(text)

    # ==========================================
    # Stop Speaking
    # ==========================================

    def stop(self):

        stop()

    # ==========================================
    # Check Speaking
    # ==========================================

    def speaking(self):

        return speaking()