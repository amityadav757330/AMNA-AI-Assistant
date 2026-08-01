import json
import os

# Get the project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Path to memory.json
MEMORY_FILE = os.path.join(BASE_DIR, "data", "memory.json")
print(MEMORY_FILE)

def load_memory():
    """
    Load memory from memory.json
    """

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({}, f, indent=4)

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    """
    Save memory to memory.json
    """

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(key, value):
    """
    Remember something.
    """

    memory = load_memory()

    memory[key.lower()] = value

    save_memory(memory)

    return f"Okay Amit, I'll remember that your {key} is {value}."


def recall(key):
    """
    Recall saved memory.
    """

    memory = load_memory()

    key = key.lower()

    if key in memory:
        return memory[key]

    return None


def forget(key):
    """
    Forget saved memory.
    """

    memory = load_memory()

    key = key.lower()

    if key in memory:
        del memory[key]

        save_memory(memory)

        return f"I forgot your {key}."

    return f"I don't remember any {key}."


def show_all_memory():
    """
    Show everything stored.
    """

    memory = load_memory()

    if len(memory) == 0:
        return "I don't remember anything yet."

    result = ""

    for key, value in memory.items():
        result += f"{key.title()} : {value}\n"

    return result.strip()


def clear_memory():
    """
    Delete everything.
    """

    save_memory({})

    return "All memory has been cleared."