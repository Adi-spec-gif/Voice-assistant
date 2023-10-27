import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I encountered an error. Please check your internet connection.")
        return ""

def main():
    speak("Hello, I'm your voice assistant. How can I help you today?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "what's the time" in command:
            # You can enhance this by getting the current time
            speak("I'm sorry, I can't provide the current time at the moment.")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day.")
            break

if __name__ == "__main__":
    main()
