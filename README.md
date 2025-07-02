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

```
---
###2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```
---
###3. Install Requirements

```bash
pip install -r requirements.txt
```
---
###🔐 Environment Variables
Create a .env file with your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key
```
---
📊 Google Sheets Setup:

-  Create a Google Sheet (e.g. VoiceAI Logs)
-  Add this header row: Timestamp | User Input | GPT Reply
-  Go to Google Cloud Console
-  Enable Google Sheets API and Google Drive API
-  Create a service account
-  Download the creds.json key file
-  Share the Google Sheet with the service account’s client email (Editor access)
- Place creds.json in the project folder (but do not commit it)

🧠 How to Run
```bash
python main.py
```
Then:
Speak into your mic,
Wait for the reply.
Say "exit" to stop the program


