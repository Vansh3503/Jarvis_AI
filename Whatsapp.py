import pyttsx3
import pywhatkit
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init('sapi5')
# text to voice pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("Vansh Said: {} \n".format(query))

    except Exception as e:
        speak("Say That Again....")
        return "None"
    return query


strTime = int(datetime.now().strftime("%H"))

update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


def sendMessage():
    speak("Who do you want to message")
    a = int(input('''Rahil -1 Vrushti 2-2 Ayushi 3-3 Zeel 4-4 '''))
    if a == 1:
        speak("Whats the Message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+917046457511", message, time_hour=strTime, time_min=update)
    elif a == 2:
        speak("Whats the Message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+919913436058", message, time_hour=strTime, time_min=update)

    elif a == 3:
        speak("Whats the Message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+919978319456", message, time_hour=strTime, time_min=update)

    elif a == 4:
        speak("Whats the Message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+917575097982", message, time_hour=strTime, time_min=update)


