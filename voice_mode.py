import keyboard
import threading
import time

from assistant.engine import AssistantEngine
from assistant.speak import stop


running = True

engine = AssistantEngine()


def start():

    engine.start_conversation()


def conversation_thread():

    if engine.conversation.active:
        print("Conversation already running.")
        return

    threading.Thread(
        target=start,
        daemon=True
    ).start()


def stop_speaking():

    stop()


def exit_program():

    global running

    running = False

    stop()

    print("\nGoodbye Amit!")


print("=" * 45)
print("          AMNA AI Assistant")
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