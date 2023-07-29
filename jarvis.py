import datetime
from email import message
import webbrowser
import openai
from apikey import api_data
import cv2
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from google.cloud import dialogflow_v2 as dialogflow

from google.oauth2 import service_account


from numpy import tile
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pyttsx3
import speech_recognition

import requests
from bs4 import BeautifulSoup
import os
import speedtest
import pyautogui
import random
from plyer import notification
from pygame import mixer
from pygame import mixer
from requests import get

openai.api_key = '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'
from INTRO import play_gif



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")
import uuid

# Generate a unique session ID
session_id = str(uuid.uuid4())


def get_dialogflow_response(query):
    session_client = dialogflow.SessionsClient.from_service_account_json(
        'jarvis-393316-3507a4863435.json')
    session = session_client.session_path('jarvis-393316', 'session_id')
    text_input = dialogflow.TextInput(text=query, language_code='en')
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text




def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    generated_text = response.choices[0].text.strip()
    return generated_text


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def analyze_sentiment(query):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(query)

    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment_label = 'Positive'
    elif compound_score <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    return sentiment_label, sentiment_scores


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
       
        generated_text = get_dialogflow_response(query)
        speak(generated_text)
        print(generated_text)


                       

        if "wake up" in query:
            from GreetMe import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break

                    #################### JARVIS: THe Trilogy 2.0 #####################

               

                elif "sentiment analysis" in query:
                    speak("Analyze your Sentiment Babyy!!")

                    while True:
                        text_prompt = takeCommand()
                        if "exit" in text_prompt:
                            break

                        sentiment_label, sentiment_scores = analyze_sentiment(text_prompt)

                        speak(sentiment_label)
                        print("Sentiment Scores: ", sentiment_scores)




                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "who is your boss" in query:
                    speak(" my boss is Vansh Malhotra. Haven't you heard his name before.")



                elif "what you can do" in query:
                    speak(" Sir! can do alot of things!")
                    print("1)Wake Up\n")
                    print("2)Sign of\n")
                    print("3)Focus Mode\n")
                    print("4)Basic Commands like Hi,hello,thankyou\n")
                    print("5)Play,Pause,Mute,Volume Up,Volume Down\n")
                    print("6)Google Anything\n")
                    print("7)Youtube Anything\n")
                    print("8)Wikipedia Anything\n")
                    print("9)Open AND Close any Software that in your Computer\n")
                    print("10)Rock,Paper,Scissor Game\n")
                    print("11)News\n")
                    print("12)Screenshot\n")
                    print("13)Click a Photo\n")
                    print("14)Temperature\n")
                    print("15)Schedule my Day\n")
                    print("16)Show your Schedule\n")
                    print("17)Go to Sleep(Offline Mode)\n")
                    print("18)Time\n")
                    print("19)Remember That\n")
                    print("20)What Do you Remember\n")
                    print("21)Tired\n")
                    print("22)Set an Alarm\n")
                    print("23)Open Camera\n")
                    print("24)Where am I\n")
                    print("25)Send Whatsapp Message\n")
                    print("26)Battery\n")
                    print("27)Ip address\n")
                    print("28)Sentiment Analysis")
                    print("29)Shutdown\n")
                 


                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")




                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )


                elif "focus mode" in query:
                    a = int(input("Are you Sure that you want to enter focus mode:-[1 for YES/2 for NO"))
                    if a == 1:
                        speak("Entering the Focus Mode")
                        os.startfile("FocusMode.py")
                        exit()
                    else:
                        exit()

               

                


                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video Paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video Played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video Muted")

                elif "volume up" in query:
                    from keyboard import volumeup

                    speak("Turning Volume up,Sir!")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown

                    speak("Turning volume down,Sir!")
                    volumedown()



                elif "open" in query:
                    from Dictapp import openappweb

                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb

                    closeappweb(query)



                elif "game" in query:
                    from game import game_play

                    game_play()

                elif "google" in query:
                    from SearchNow import searchGoogle

                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube

                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia

                    searchWikipedia(query)
                elif "news" in query:
                    from NewsRead import latestnews

                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import Wolframalpha
                    from Calculatenumbers import Calc

                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("Smile")
                    pyautogui.press("enter")




                elif "temperature" in query:
                    search = "temperature in Ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strTime}")

                elif "sign of" in query:
                    speak("Going to Sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to " + rememberMessage)
                    remember = open("rememberthat.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("rememberthat.txt", "r")
                    speak("You told me " + remember.read())

                elif "tired" in query:
                    speak("Playing your Favourite Songs")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=WgOhlwxU7eE")
                    elif b == 2:
                        webbrowser.open("https://open.spotify.com/track/0og9wKFGgFFNQnrBe7eisG?si=e01e07e10018469c")

                    elif b == 3:
                        webbrowser.open("https://open.spotify.com/track/0iXLwnLmLwn9y54JtBTNxY?si=10a810feb5634dd0")
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "send whatsapp message" in query:
                    from Whatsapp import sendMessage

                    sendMessage()





                elif "open camera" in query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(5)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif 'where i am' in query:
                    speak("Wait Sir,let me check")
                    try:
                        ip = get('https://api.ipify.org').text
                        print(ip)
                        url = 'https://get.geojs.io/v1/op/geo/' + ip + '.json'
                        geo_req = requests.get(url)
                        geo_data = geo_req.json()
                        city = geo_data['city']
                        country = geo_data['country']
                        speak(f"Sir you are in {city} city of {country} country")
                    except:
                        speak("Sorry Sir! Location Not Found")
                        pass


                elif "battery" in query:
                    import psutil

                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"Sir our System have {percentage} percent battery")

                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"Your IP address is {ip}")

                elif "shutdown" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer?{yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                elif "exit" in query:
                    exit()
