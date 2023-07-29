import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
# text to voice pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def greetMe():
    hour=int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning Mr Vansh")
        
    elif hour > 12 and hour < 18:
        speak("Good Afternoon Mr Vansh")
        
    else:
        speak("Good Evening Mr Vansh")
      

    