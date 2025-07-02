import speech_recognition as sr
import pyttsx3

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
