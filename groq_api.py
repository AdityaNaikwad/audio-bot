import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-70b-8192"

def get_groq_response(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": GROQ_MODEL
    }

    res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]
