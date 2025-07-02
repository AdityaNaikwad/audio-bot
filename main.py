from speech_module import listen_to_user, speak
from groq_api import get_groq_response
from logger import log_to_google_sheet

def run_voice_ai():
    print("🎤 Voice AI is running. Say 'exit' to quit.")
    speak("Hi! I am your AI assistant. Say something, or say 'exit' to quit.")

    while True:
        try:
            user_input = listen_to_user()

            if not user_input:
                speak("Sorry, I didn't catch that. Please try again.")
                continue

            if user_input.lower() == "exit":
                speak("Goodbye! Have a great day.")
                print(" Exiting...")
                break

            print("You said:", user_input)
            gpt_reply = get_groq_response(user_input)
            print("GPT says:", gpt_reply)

            speak(gpt_reply)
            log_to_google_sheet(user_input, gpt_reply)

        except Exception as e:
            print("Error:", str(e))
            speak("Something went wrong. Please try again.")

if __name__ == "__main__":
    run_voice_ai()

