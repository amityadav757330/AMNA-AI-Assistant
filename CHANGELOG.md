# Changelog

All notable changes to this project will be documented in this file.

---

# v0.5.0 (Current Release)

## Added

- Modular Intent Architecture
- Router System
- Memory Intent
- Search Intent
- System Intent
- Info Intent
- AI Intent
- Service Layer
- Continuous Conversation
- Edge TTS
- Ollama Integration

---

## Memory

Added

- Remember
- Recall
- Forget
- Persistent Memory

---

## Search

Added

- Google Search
- YouTube Search
- Weather
- News
- Wikipedia Search

---

## Desktop Automation

Added

- Chrome
- VS Code
- PyCharm
- Calculator
- Notepad
- Downloads
- Documents
- Desktop

---

## System Controls

Added

- Shutdown
- Restart
- Lock PC
- Cancel Shutdown

---

## Voice

Improved

- Faster TTS
- Better Speech Recognition
- Continuous Conversation
- Goodbye Handling
- Stop Speaking

---

## Refactoring

Major project refactor.

Old Architecture

```
Conversation
        ↓
Brain
```

New Architecture

```
Conversation
        ↓
AI Service
        ↓
Brain
        ↓
Router
        ↓
Intents
        ↓
Services
```

---

## Files Added

```
router.py
memory_intents.py
system_intents.py
search_intents.py
info_intents.py
ai_intents.py

memory_service.py
ai_service.py
```

---

## Files Refactored

```
brain.py
conversation.py
engine.py
voice_mode.py
```

---

## Status

Checkpoint 4 Completed

Architecture Stable

Ready for Checkpoint 5

---

# Upcoming (v0.6)

- Smart Memory
- User Profile
- Context Awareness
- Automatic Learning

---

# Upcoming (v0.7)

- Wake Word

---

# Upcoming (v0.8)

- Vision
- OCR

---

# Upcoming (v0.9)

- GUI

---

# Upcoming (v1.0)

- Production Release
- Installer
- Plugin System
- Automation