import time

from assistant.speech import listen
from assistant.brain import reply
from assistant.speak import speak


WAKE_WORDS = [
    "amna",
    "hey amna",
    "hello amna",
    "ok amna",
    "okay amna"
]

SLEEP_WORDS = [
    "go to sleep",
    "sleep",
    "stop listening",
    "bye",
    "bye amna",
    "goodbye"
]

AUTO_SLEEP_TIME = 60  # seconds


def remove_wake_word(text):
    """
    Remove wake word from beginning of sentence.
    """

    for wake in WAKE_WORDS:

        if text.startswith(wake):

            return text[len(wake):].strip(" ,")

    return text


def start():

    awake = False

    last_activity = time.time()

    speak("AMNA is ready.")

    while True:

        # ==========================================
        # Sleeping
        # ==========================================

        if not awake:

            print("😴 Waiting for wake word...")

            text = listen()

            if not text:
                continue

            text = text.lower().strip()

            matched = False

            for wake in WAKE_WORDS:

                if text.startswith(wake):

                    matched = True
                    awake = True
                    last_activity = time.time()

                    command = remove_wake_word(text)

                    # User only said "Amna"
                    if command == "":
                        speak("Yes Amit.")
                        break

                    # Execute immediately
                    response = reply(command)
                    print(f"AMNA: {response}")
                    speak(response)

                    break

            if matched:
                continue

        # ==========================================
        # Active Conversation
        # ==========================================

        if time.time() - last_activity > AUTO_SLEEP_TIME:

            speak("Going to sleep.")

            awake = False

            continue

        print("🎤 Listening...")

        command = listen()

        if not command:
            continue

        last_activity = time.time()

        command = command.lower().strip()

        if any(word in command for word in SLEEP_WORDS):

            speak("Going to sleep.")

            awake = False

            continue

        response = reply(command)

        print(f"AMNA: {response}")

        speak(response)