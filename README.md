# 🧠 Voice AI Demo with Groq & Google Sheets Logging

A voice-based AI assistant that:
- Takes your **voice input**
- Uses **Groq's blazing-fast LLaMA3-70B** to generate a smart response
- Speaks the response aloud using **text-to-speech**
- Logs the entire conversation to **Google Sheets**

---

## 🚀 Features

- 🎤 Real-time voice input via microphone
- ⚡ GPT response using Groq (LLaMA3-70B-8192)
- 🗣️ Voice reply via `pyttsx3` (offline text-to-speech)
- 📊 Logs every question & answer to a **Google Sheet**
- 🛑 Say “exit” to quit at any time

---

## 🧰 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Groq API](https://console.groq.com/)
- `speechrecognition` + `pyaudio`
- `pyttsx3` for TTS
- `gspread` + `oauth2client` for Google Sheets
- `.env` for managing secrets

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com//voice-ai-groq-demo.git
cd voice-ai-groq-demo
