"""
=========================================
AMNA AI Assistant
Wake Word System
=========================================
"""

from assistant.voice.speech import listen
from assistant.voice.speak import speak


# ==========================================
# Wake Words
# ==========================================

WAKE_WORDS = [
    "hey amna",
    "amna"
]


# ==========================================
# Sleep Words
# ==========================================

SLEEP_WORDS = [
    "go to sleep",
    "sleep",
    "stop listening",
    "goodbye",
    "bye amna"
]


# ==========================================
# Remove Wake Word
# ==========================================

def remove_wake_word(text):

    text = text.lower().strip()

    for word in WAKE_WORDS:

        if text.startswith(word):

            return text[len(word):].strip()

    return text


# ==========================================
# Check Wake Word
# ==========================================

def contains_wake_word(text):

    if not text:
        return False

    text = text.lower().strip()

    return any(
        text.startswith(word)
        for word in WAKE_WORDS
    )


# ==========================================
# Check Sleep Word
# ==========================================

def contains_sleep_word(text):

    if not text:
        return False

    text = text.lower().strip()

    return any(
        word in text
        for word in SLEEP_WORDS
    )


# ==========================================
# Wake Word Listener
# ==========================================

def start():

    awake = False

    speak("AMNA is ready.")

    while True:

        # ==========================================
        # Sleep Mode
        # ==========================================

        if not awake:

            print("\n😴 Waiting for wake word...")

            text = listen()

            if not text:
                continue

            print(f"You: {text}")

            if contains_wake_word(text):

                awake = True

                command = remove_wake_word(text)

                # Wake word only
                if not command:

                    speak("Yes Amit, how can I help you?")

                else:

                    return command

        # ==========================================
        # Active Mode
        # ==========================================

        else:

            print("\n🎤 Listening for command...")

            command = listen()

            if not command:
                continue

            print(f"You: {command}")

            if contains_sleep_word(command):

                speak("Going to sleep.")

                awake = False

                continue

            return command