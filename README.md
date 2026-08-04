# 🤖 AMNA AI Assistant

AMNA is a modular AI Voice Assistant built in Python. It combines voice recognition, conversational AI, long-term memory, internet search, desktop automation, and a clean software architecture.

AMNA is designed as a personal AI assistant similar to Jarvis, with a focus on scalability, maintainability, and future AI capabilities.

---

# 🚀 Features

## 🎙 Voice Assistant

- Continuous conversation
- Speech Recognition
- Edge TTS Voice
- Stop Speaking Feature
- Voice-based interaction

---

## 🧠 AI

- Ollama Integration
- LLM Chat
- Intelligent Fallback Responses
- Natural Conversations

---

## 💾 Memory

- Remember personal information
- Recall stored information
- Forget information
- Persistent memory storage

Examples:

Remember my name is Amit

What is my name?

Forget my name

---

## 🌐 Internet

- Google Search
- YouTube Search
- Weather
- News
- Wikipedia Search
- Website Opening

---

## 💻 Desktop Automation

- Open Chrome
- Open VS Code
- Open PyCharm
- Open Calculator
- Open Notepad
- Open Downloads
- Open Documents
- Open Desktop

---

## ⚙ System Controls

- Shutdown PC
- Restart PC
- Cancel Shutdown
- Lock PC

---

# 🏗 Architecture

AMNA follows a modular architecture.

```
Voice Mode
     │
Conversation
     │
AI Service
     │
Brain
     │
Router
     │
 ├── Memory Intent
 ├── System Intent
 ├── Search Intent
 ├── Info Intent
 └── AI Intent
```

---

# 📁 Project Structure

```
AMNA/
│
├── assistant/
│   ├── brain.py
│   ├── router.py
│   │
│   ├── intents/
│   │   ├── memory_intents.py
│   │   ├── system_intents.py
│   │   ├── search_intents.py
│   │   ├── info_intents.py
│   │   └── ai_intents.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── memory_service.py
│   │   ├── speech_service.py
│   │   └── ...
│   │
│   ├── llm.py
│   ├── speak.py
│   ├── speech.py
│   ├── conversation.py
│   └── engine.py
│
├── data/
├── docs/
├── logs/
├── tests/
│
├── voice_mode.py
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies

- Python 3.12
- Ollama
- Edge TTS
- SpeechRecognition
- pygame
- Requests
- DuckDuckGo Search
- Wikipedia API

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AMNA.git
```

Go to project

```bash
cd AMNA
```

Install requirements

```bash
pip install -r requirements.txt
```

Run Ollama

```bash
ollama serve
```

Start AMNA

```bash
python voice_mode.py
```

---

# ⌨ Hotkeys

| Key | Action |
|------|--------|
| F9 | Start Conversation |
| F10 | Stop Speaking |
| ESC | Exit AMNA |

---

# 📈 Current Version

## v0.5.0

✔ Modular Architecture

✔ Intent Routing

✔ Service Layer

✔ Continuous Conversation

✔ Internet Search

✔ Memory System

✔ Desktop Automation

✔ Voice Assistant

---

# 🚀 Upcoming Features

- Smart Memory
- Wake Word
- Vision
- OCR
- Face Recognition
- GUI
- Email Assistant
- WhatsApp Automation
- Calendar
- Plugin System

---

# 👨‍💻 Developer

**Amit Yadav**

Computer Science Engineering Student

GL Bajaj Institute of Technology and Management

---

# 📜 License

This project is developed for educational and portfolio purposes.