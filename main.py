import pyttsx3
import speech_recognition as sr
from arduinocont import led

import time

# make engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)   #changing index changes voices but ony 0 and 1 are working here.


def speak(text):
    engine.say(text)
    engine.runAndWait()

time.sleep(1)
speak("Hello Sir")
speak("How can I help you ?")
print("How can I help you ?")

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("How can I hep you ?")

        audio = r.listen(source)
        try:
            print("Recognizing...")
            # speak("Recognizing...")
            query = r.recognize_google(audio, language='en-ne')
        except Exception as e:
            print("I am sorry, I did not understand that.")
            speak("I am sorry, I did not understand that.")
            return "None"
        return query


if __name__ == "__main__":
    while True:
        query = myCommand().lower()
        if 'on' in query:
            print("Ok Sir, turning on the light")
            speak("Ok Sir, turning on the light")
            print("Turned on")
            led(1)
        elif 'off' in query:
            print("Ok Sir, turning off the light")
            speak("Ok Sir, turning off the light")
            print("Turned off")
            led(0)
        elif 'exit' in query:
            speak("ok goodbye ")
            print("ok good bye")
            break
