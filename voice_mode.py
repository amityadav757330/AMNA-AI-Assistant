import keyboard
import threading
import time

from assistant.conversation import Conversation
from assistant.speak import stop


running = True

conversation = Conversation()


def start_conversation():
    conversation.start()


def conversation_thread():

    if conversation.active:
        print("Conversation already running.")
        return

    thread = threading.Thread(
        target=start_conversation,
        daemon=True
    )

    thread.start()


def stop_speaking():
    stop()


def exit_program():

    global running

    running = False

    stop()

    print("\nGoodbye Amit!")


print("=" * 45)
print("          AMNA Voice Assistant")
print("=" * 45)
print("F9  -> Start Conversation")
print("F10 -> Stop Speaking")
print("ESC -> Exit")
print("=" * 45)

keyboard.add_hotkey("f9", conversation_thread)
keyboard.add_hotkey("f10", stop_speaking)
keyboard.add_hotkey("esc", exit_program)

while running:
    time.sleep(0.1)