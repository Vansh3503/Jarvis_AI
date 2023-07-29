import requests
import json
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)
import finalinterface
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service. Please check your internet connection.")
    
    return None

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=909488837ca1447eafcd16cb164a1048",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=909488837ca1447eafcd16cb164a1048",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=909488837ca1447eafcd16cb164a1048",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=909488837ca1447eafcd16cb164a1048",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=909488837ca1447eafcd16cb164a1048",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=909488837ca1447eafcd16cb164a1048"
    }

    speak("Which field news do you want? You can choose from [business], [health], [sports], [entertainment], [technology], [science].")
    field = takeCommand()
    

    if field not in apidict:
        speak("I'm sorry, that's not a valid category. Please choose a valid category.")
        return

    url = apidict[field]
    news = requests.get(url).json()

    if news.get("status") != "ok" or not news.get("articles"):
        speak("I'm sorry, I couldn't fetch the news for the selected category.")
        return

    articles = news["articles"]
    speak(f"Here are the latest {field} news.")

    for idx, article in enumerate(articles, 1):
        title = article["title"]
        url = article["url"]
        print(f"{idx}. {title}")
        speak(title)
        print("For more info visit:", url)
        speak("For more info visit the link provided.")

        if idx < len(articles):
            speak("Do you want to hear the next news? Please say 'yes' or 'no'.")
            response = takeCommand()
            if "no" in response:
                speak("Alright, stopping the news updates.")
                break
            elif "yes" not in response:
                speak("Sorry, I didn't get that. Continuing with the next news.")

    speak("That's all for now. Thank you!")

      