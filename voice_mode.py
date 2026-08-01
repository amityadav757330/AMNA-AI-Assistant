import keyboard
import threading
import time

from assistant.speech import listen
from assistant.brain import reply
from assistant.speak import speak, stop


running = True


def start_conversation():

    print("\n🎤 Listening...")

    listen_start = time.time()

    text = listen()

    listen_end = time.time()

    print(f"⏱ Listening : {listen_end-listen_start:.2f} sec")

    if not text:
        speak("I didn't hear anything.")
        return

    think_start = time.time()

    response = reply(text)

    think_end = time.time()

    print(f"🧠 Thinking : {think_end-think_start:.2f} sec")

    speak(response)


def conversation_thread():

    thread = threading.Thread(
        target=start_conversation,
        daemon=True
    )

    thread.start()


def exit_program():

    global running

    running = False

    stop()

    print("\nGoodbye Amit!")


print("=" * 45)
print("          AMNA Voice Assistant")
print("=" * 45)
print("F9  -> Talk")
print("F10 -> Stop Speaking")
print("ESC -> Exit")
print("=" * 45)

keyboard.add_hotkey("f9", conversation_thread)
keyboard.add_hotkey("f10", stop)
keyboard.add_hotkey("esc", exit_program)

while running:
    time.sleep(0.1)