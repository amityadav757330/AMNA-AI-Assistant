import json
from pathlib import Path

# ===============================
# Memory Directory
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent

MEMORY_DIR = BASE_DIR / "data" / "memory"

PROFILE_FILE = MEMORY_DIR / "profile.json"
PREFERENCES_FILE = MEMORY_DIR / "preferences.json"
CONTEXT_FILE = MEMORY_DIR / "context.json"
CONVERSATION_FILE = MEMORY_DIR / "conversation.json"


# ===============================
# Generic Functions
# ===============================

def _load(file_path):

    if not file_path.exists():
        return {}

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except:

        return {}


def _save(file_path, data):

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ===============================
# Profile
# ===============================

def get_profile():

    return _load(PROFILE_FILE)


def save_profile(profile):

    _save(PROFILE_FILE, profile)


# ===============================
# Preferences
# ===============================

def get_preferences():

    return _load(PREFERENCES_FILE)


def save_preferences(pref):

    _save(PREFERENCES_FILE, pref)


# ===============================
# Context
# ===============================

def get_context():

    return _load(CONTEXT_FILE)


def save_context(context):

    _save(CONTEXT_FILE, context)


def clear_context():

    _save(CONTEXT_FILE, {})


# ===============================
# Conversation Memory
# ===============================

def get_conversation():

    return _load(CONVERSATION_FILE)


def save_conversation(data):

    _save(CONVERSATION_FILE, data)