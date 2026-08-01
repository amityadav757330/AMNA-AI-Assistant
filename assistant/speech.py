import speech_recognition as sr

recognizer = sr.Recognizer()

# Fast recognition settings
recognizer.dynamic_energy_threshold = True
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.3


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

        except sr.WaitTimeoutError:
            return ""

    # First try English / Hinglish
    try:

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:
        pass

    except sr.RequestError:
        pass

    # If English fails, try Hindi
    try:

        text = recognizer.recognize_google(
            audio,
            language="hi-IN"
        )

        print("You:", text)

        return text.lower()

    except:
        return ""