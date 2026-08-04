# 🏗️ AMNA Architecture

## Overview

AMNA is a modular AI voice assistant built using Python. Each feature is implemented as an independent module so the project remains scalable and easy to maintain.

---

## Current Architecture

```
                voice_mode.py
                      │
                      ▼
             Assistant Engine
                      │
        ┌─────────────┼─────────────┐
        │             │             │
 Conversation      Memory       Future Modules
        │
        ▼
      Brain
        │
        ▼
      Ollama
        │
        ▼
      Response
        │
        ▼
     Edge TTS
```

---

## Current Modules

### Engine
Coordinates all assistant modules.

### Conversation
Handles continuous conversations.

### Brain
Processes commands and decides how AMNA should respond.

### Speech Recognition
Converts voice into text.

### Text To Speech
Converts AI responses into natural speech.

### Memory
Stores user information and preferences.

---

## Future Modules

- Wake Word
- Vision
- OCR
- Internet Search
- Desktop Automation
- GUI
- AI Agent

---

## Design Goals

- Modular
- Easy to maintain
- Easy to extend
- Professional architecture
- Open-source friendly