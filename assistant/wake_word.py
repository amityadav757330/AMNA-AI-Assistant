from assistant.speech import listen
from assistant.brain import reply
from assistant.speak import speak

WAKE_WORDS = ["hey amna", "amna"]

SLEEP_WORDS = [
    "go to sleep",
    "sleep",
    "stop listening",
    "goodbye",
    "bye amna"
]


def start():
    awake = False

    speak("AMNA is ready.")

    while True:

        # Sleep Mode
        if not awake:
            print("😴 Waiting for wake word...")

            text = listen()

            if not text:
                continue

            if any(word in text for word in WAKE_WORDS):
                awake = True
                speak("Yes Amit, how can I help you?")

        # Active Mode
        else:
            print("🎤 Listening for command...")

            command = listen()

            if not command:
                continue

            if any(word in command for word in SLEEP_WORDS):
                speak("Going to sleep.")
                awake = False
                continue

            response = reply(command)
            speak(response)