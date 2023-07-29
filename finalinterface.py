import typing
import PyQt5
import sys

from PyQt5.QtWidgets import QWidget, QTextEdit, QApplication, QMessageBox
from datetime import timedelta
from datetime import datetime
from PyQt5.QtWidgets import QWidget,QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
import pywhatkit
from JarvisFinal import Ui_Form
from PyQt5.QtCore import QThread
import pygame
import datetime
from email import message
import webbrowser
import openai
import requests
import cv2
from geopy.geocoders import Nominatim
pygame.mixer.init()
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from google.cloud import dialogflow_v2 as dialogflow
import time
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

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

class GuiofJarvis(QWidget):
    def __init__(self):
        super(GuiofJarvis,self).__init__()
        self.finalinterfaceUI=Ui_Form()
        self.finalinterfaceUI.setupUi(self)
        self.finalinterfaceUI.start_button_2.clicked.connect(self.close)
        self.finalinterfaceUI.start_button_3.clicked.connect(self.manualprint)

        self.runAllmovies()

        
    def terminalprint(self, *args):
        text = " ".join(map(str, args))
        self.finalinterfaceUI.textEdit.insertPlainText(text)
    def show_loading_animation(self):
        # Show a loading animation or message to indicate Jarvis is initializing.
        speak("Initializing Jarvis. Please wait a moment.")
        self.terminalprint("Initializing Jarvis. Please wait a moment.")
        # Code to show a loading animation if desired.    

    def runAllmovies(self):
         
        self.finalinterfaceUI.movie=QtGui.QMovie("gyhf.jpg")
        self.finalinterfaceUI.DOUBLE.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("B.G_Template_1.gif")
        self.finalinterfaceUI.P1.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("__1.gif")
        self.finalinterfaceUI.P2.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("initial.gif")
        self.finalinterfaceUI.P3.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("wave.gif")
        self.finalinterfaceUI.label_3.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("Jarvis_Gui (1).gif")
        self.finalinterfaceUI.label.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("__1.gif")
        self.finalinterfaceUI.sleeping.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        self.finalinterfaceUI.movie=QtGui.QMovie("ggg.gif")
        self.finalinterfaceUI.speak.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        
        self.finalinterfaceUI.movie=QtGui.QMovie("live.gif")
        self.finalinterfaceUI.label_2.setMovie(self.finalinterfaceUI.movie)
        self.finalinterfaceUI.movie.start()

        startEcecution.start()
    def updatemovie(self,state):
        if state=="listening":
            self.finalinterfaceUI.P2.raise_()
            self.finalinterfaceUI.sleeping.hide()
            self.finalinterfaceUI.speak.hide()
            self.finalinterfaceUI.P2.show()
        
        if state=="speaking":
            self.finalinterfaceUI.speak.raise_()
            self.finalinterfaceUI.sleeping.hide()
            self.finalinterfaceUI.P2.hide()
            self.finalinterfaceUI.speak.show()
        
        if state=="sleeping":
            self.finalinterfaceUI.sleeping.raise_()
            self.finalinterfaceUI.speak.hide()
            self.finalinterfaceUI.P2.hide()
            self.finalinterfaceUI.sleeping.show()
        

        
    
    def handle_focus_mode(self):
        # Implement the logic to enter focus mode here
        # For example, you can display a message and execute the focus mode functionality.
        speak("Entering the Focus Mode")
        os.startfile("FocusMode.py")

    
    def get_input(self):
        return self.input_line_edit.text()


    def manualprint(self):
       
        cmd = self.finalinterfaceUI.entecomm.text()
       
        if cmd:
            self.finalinterfaceUI.entecomm.clear()
            self.finalinterfaceUI.textEdit.insertPlainText(f"{cmd}")
        
            if cmd == 'exit':
                ui.close()
            elif cmd == 'help':
                speak("\nI can Perform various tasks which is programmed inside me by Vansh Sir.\n"
                               "Examples are: Time, Wikipedia, Google, Whatsapp Message, Focus Mode, Schedule, Alarm, etc.\n"
                               "Sleep well or else I will chit chat.\n")
                self.terminalprint("\nI can Perform various tasks which is programmed inside me by Vansh Sir.\n"
                               "Examples are: Time, Wikipedia, Google, Whatsapp Message, Focus Mode, Schedule, Alarm, etc.\n"
                               "Sleep well or else I will chit chat.\n")
            if "focus mode" in cmd:
                pass
        else:
            pass


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
    fulfillment_text = response.query_result.fulfillment_text

    # Add a new line character to the fulfillment text
    fulfillment_text += "\n"

    return fulfillment_text


def initialize_engine():
    # ... (Your existing code)
        
    # Initialize the pygame.mixer module
        pygame.mixer.init()
        
        return engine

def play_music(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    generated_text = response.choices[0].text.strip()
    return generated_text


def speak(audio):
    ui.updatemovie("sleeping")
    engine.say(audio)
    engine.runAndWait()

import requests

import requests

def get_weather(city):
    api_key = '4c8588e6f2a44188833101859232307'
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(base_url)
    data = response.json()

    if "error" in data:
        return f"Sorry, there was an error retrieving weather information for {city}."

    current = data.get("current")
    if not current or "temp_c" not in current or "condition" not in current:
        return f"Sorry, I couldn't find weather information for {city}."
    
    temperature = current["temp_c"]
    description = current["condition"]["text"]
    return f"Current temperature in {city} is {temperature}°C with {description}."

def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    joke = f"{data['setup']} {data['punchline']}"
    return joke


def alarm(query):
    timehere = open("alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def get_location(query):
    geolocator = Nominatim(user_agent="jarvis")
    location = geolocator.geocode(query)
    if location:
        return location.address, location.latitude, location.longitude
    else:
        return None, None, None

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



class mainFile(QThread):
    def __init__(self):
        super(mainFile,self).__init__()
    
    def latestnews(self):
        apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=909488837ca1447eafcd16cb164a1048",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=909488837ca1447eafcd16cb164a1048",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=909488837ca1447eafcd16cb164a1048",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=909488837ca1447eafcd16cb164a1048",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=909488837ca1447eafcd16cb164a1048",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=909488837ca1447eafcd16cb164a1048"
                }

        speak("Which field news do you want? You can choose from [business], [health], [sports], [entertainment], [technology], [science].")
        field = self.takeCommand().lower()
    
        if field not in apidict:
            speak("I'm sorry, that's not a valid category. Please choose a valid category.")
            exit()
        url = apidict[field]
        try:
            news = requests.get(url).json()
            if news.get("status") != "ok" or not news.get("articles"):
                speak("I'm sorry, I couldn't fetch the news for the selected category.")
                return self.latestnews()

            articles = news["articles"]
            speak(f"Here are the latest {field} news.")

            for idx, article in enumerate(articles, 1):
                title = article["title"]
                url = article["url"]
                ui.terminalprint(f"{idx}. {title}\n")
                speak(title)
                ui.terminalprint("For more info visit:\n", url)
                speak("For more info visit the link provided.")
            

                if idx < len(articles):
                    speak("Do you want to hear the next news? Please say 'yes' or 'no'.")
                    response = self.takeCommand().lower()
                    if "no" in response:
                        speak("Alright, stopping the news updates.")
                        break
                    elif "yes" not in response:
                        speak("Sorry, I didn't get that. Continuing with the next news.")

            speak("That's all for now. Thank you!")
        except requests.exceptions.RequestException:
            speak("I'm sorry, there was an error fetching the news. Please check your internet connection.")
    
    
    
    def game_play(self):
        speak("Avengers Assemble !!")
        print("LETS PLAYYYYYYYYYYYYYY")
        i = 0
        Me_score = 0
        Com_score = 0
        while (i < 5):
            choose = ("rock", "paper", "scissors")  # Tuple
            com_choose = random.choice(choose)
            query = self.takeCommand().lower()
            if (query == "rock"):
                if (com_choose == "rock"):
                    speak("ROCK")
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                elif (com_choose == "paper"):
                    speak("paper")
                    Com_score += 1
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    speak("Scissors")
                    Me_score += 1
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

            elif (query == "paper"):
                if (com_choose == "rock"):
                    speak("ROCK")
                    Me_score += 1
                    ui.terminalprint(f"Score:- ME :- {Me_score + 1} : COM :- {Com_score}")

                elif (com_choose == "paper"):
                    speak("paper")
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    speak("Scissors")
                    Com_score += 1
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

            elif (query == "scissors" or query == "scissor"):
                if (com_choose == "rock"):
                    speak("ROCK")
                    Com_score += 1
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                elif (com_choose == "paper"):
                    speak("paper")
                    Me_score += 1
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    speak("Scissors")
                    ui.terminalprint(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            i += 1

        print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")







    def run(self):
        self.runJarvis()

    
    def takeCommand(self):
                
                          
        ui.updatemovie("listening")
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            ui.terminalprint("Listening.....\n")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)

        try:
            ui.updatemovie("speaking")
            ui.terminalprint("Understanding..\n")
            query = r.recognize_google(audio, language='en-in')
            ui.terminalprint(f"You Said: {query}\n")
        except Exception as e:
            ui.terminalprint("Say that again\n")
            time.sleep(3) 
            return "None"
        return query





    def runJarvis(self):
        
        play_music("JARVIS START UP.mp3")
        while pygame.mixer.music.get_busy():
            continue
        
        from GreetMe import greetMe
        greetMe()
        date=datetime.datetime.today().strftime("%Y-%m-%d")

        speak(f'Sir Todays Date is {date}')
        ui.terminalprint(f"Sir Today's Date is {date}\n")
        day = datetime.datetime.now().strftime("%A")
        speak(f"Sir Today is {day}")
        ui.terminalprint(f"Today is {day}\n")
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f" Boss The time is {strTime}")
        ui.terminalprint(f" Boss The time is {strTime}\n")

        city = "Ahmedabad"  # You can modify this to extract the city from the query.
        weather_info = get_weather(city)
        ui.terminalprint(weather_info + "\n")

        speak(weather_info)
        speak("Greetings, hero of the digital realm! I am Jarvis, programmed to be your ultimate sidekick in the real world")
        
        
        

        while True:
         
       
            
            query = self.takeCommand().lower()
            if "exit" in query:
                exit()
       
            generated_text = get_dialogflow_response(query)
            speak(generated_text)
            ui.terminalprint(generated_text)

            if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    while True:
                        query=self.takeCommand().lower()
                        if "exit" in query:
                            break
              
                       

            if "wake up" in query:
                play_music("digital.mp3")
                while pygame.mixer.music.get_busy():
                    continue
                speak("\n You can Perform various tasks which is programmed inside me by Vansh Sir.\n"
                            "Examples are: Time, Wikipedia, Google, Whatsapp Message, Focus Mode, Schedule, Alarm and many more .\n"
                               "Give Command or else i will sleep.\n")
            
                     
                        



            

                while True:
                    query = self.takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can call me anytime")
                        break

                    #################### JARVIS: THe Trilogy 2.0 #####################

               

                    elif "sentiment analysis" in query:
                        speak("Analyze your Sentiment Babyy!!")

                        while True:
                            text_prompt = self.takeCommand().lower()
                            if "exit" in text_prompt:
                                break

                            sentiment_label, sentiment_scores = analyze_sentiment(text_prompt)

                            speak(sentiment_label)
                            ui.terminalprint("Sentiment Scores: ", sentiment_scores)

                    elif "joke" in query:
                        joke = get_random_joke()
                        ui.terminalprint(joke)
                        speak(joke)

                        


                    elif "search location" in query:
                        location_query = query.replace("search location", "").strip()
                        address, latitude, longitude = get_location(location_query)
                        if address:
                            speak(f"Location found: {address}")
                            ui.terminalprint(f"Location found: {address}")
                        else:
                            speak("Sorry, I couldn't find the location.")
                            ui.terminalprint("Sorry, I couldn't find the location.")

                    elif "who is your boss" in query:
                        speak(" my boss is Vansh Malhotra. Haven't you heard his name before.")



                    elif "what you can do" in query:
                        speak(" Sir! can do alot of things!")
                        ui.terminalprint("1)Wake Up\n")
                        ui.terminalprint("2)Sign of\n")
                        ui.terminalprint("3)Focus Mode\n")
                        ui.terminalprint("4)Basic Commands like Hi,hello,thankyou\n")
                        ui.terminalprint("5)Play,Pause,Mute,Volume Up,Volume Down\n")
                        ui.terminalprint("6)Google Anything\n")
                        ui.terminalprint("7)Youtube Anything\n")
                        ui.terminalprint("8)Wikipedia Anything\n")
                        ui.terminalprint("9)Open AND Close any Software that in your Computer\n")
                        ui.terminalprint("10)Rock,Paper,Scissor Game\n")
                        ui.terminalprint("11)News\n")
                        ui.terminalprint("12)Screenshot\n")
                        ui.terminalprint("13)Click a Photo\n")
                        ui.terminalprint("14)Temperature\n")
                        ui.terminalprint("15)Schedule my Day\n")
                        ui.terminalprint("16)Show your Schedule\n")
                        ui.terminalprint("17)Go to Sleep(Offline Mode)\n")
                        ui.terminalprint("18)Time\n")
                        ui.terminalprint("19)Remember That\n")
                        ui.terminalprint("20)What Do you Remember\n")
                        ui.terminalprint("21)Tired\n")
                        ui.terminalprint("22)Set an Alarm\n")
                        ui.terminalprint("23)Open Camera\n")
                        ui.terminalprint("24)Where am I\n")
                        ui.terminalprint("25)Send Whatsapp Message\n")
                        ui.terminalprint("26)Battery\n")
                        ui.terminalprint("27)Ip address\n")
                        ui.terminalprint("28)Sentiment Analysis")
                        ui.terminalprint("29)Joke")
                        ui.terminalprint("29)Shutdown\n")
                 


                    elif "schedule my day" in query:
                        tasks = []  # Empty list
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = self.takeCommand().lower()
                        if "yes" in query:
                            file = open("tasks.txt", "w")
                            file.write(f"")
                            file.close()
                            speak("Please speak the number of tasks:")
                            no_tasks = int(self.takeCommand())
                            i = 0
                            for i in range(no_tasks):
                                speak(f"Please speak task {i + 1}:")
                                task = self.takeCommand()
                                tasks.append(task)
                                file = open("tasks.txt", "a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            speak("Please speak the number of tasks:")
                            no_tasks = int(self.takeCommand())
                            for i in range(no_tasks):
                                speak(f"Please enter task {i + 1}:")
                                task = self.takeCommand()
                                tasks.append(task)
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

                    
                    
                    elif "weather" in query:
                        city = query.split("weather in ")[-1]
                        weather_info = get_weather(city)
                        if weather_info:
                            ui.terminalprint(weather_info)
                            speak(weather_info)

                        else:
                            speak("Sorry, I couldn't find weather information for the specified city.")
                           


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
                        
                            speak("Entering the Focus Mode")
                            os.startfile("FocusMode.py")
                            exit()
                    

            

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
                       self.game_play()

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
                     
                        self.latestnews()

                    

                    elif "calculate" in query:
                        from Calculatenumbers import Wolframalpha
                        from Calculatenumbers import Calc

                        query = query.replace("calculate", "")
                        query = query.replace("jarvis", "")
                        Calc(query)

                    elif "screenshot" in query:
                        im = pyautogui.screenshot()
                        im.save("Jarvis Screenshot.jpg")

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
                        ui.terminalprint("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")
                    elif "send whatsapp message" in query:
                        speak("The Contacts saved in my Database are :Vegeta(Rahil),Vrushti,Ayushi,Zeel,Vp,Mom,Dad,Nisarg")
                        strTime = int(datetime.now().strftime("%H"))

                        update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


                        speak("Who do you want to message")
                        a = self.takeCommand.lower()
                        if "vegeta" in a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+917046457511", message, time_hour=strTime, time_min=update)
                        
                        elif "baby" in a:
                            speak("Whats the Message")
                            message = self.takeCommand()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+919913436058", message, time_hour=strTime, time_min=update)

                        elif "ayushi" in a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+919978319456", message, time_hour=strTime, time_min=update)

                        elif "zeel" in  a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+917575097982", message, time_hour=strTime, time_min=update)

                        elif "dad" in  a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+919825025582", message, time_hour=strTime, time_min=update)

                        elif "mom" in  a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+919099147514", message, time_hour=strTime, time_min=update)

                        elif "nisarg" in  a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+919313346308", message, time_hour=strTime, time_min=update)

                        elif "vp" in  a:
                            speak("Whats the Message")
                            message = self.takeCommand().lower()
                            ui.terminalprint(message)
                            pywhatkit.sendwhatmsg("+91", message, time_hour=strTime, time_min=update)



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
                        speak("Wait Sir, let me check")
                        try:
                            ip = requests.get('https://api.ipify.org').text
                            print("IP Address:", ip)

                            url = 'https://get.geojs.io/v1/op/geo/' +'2406:b400:d5:ba5a:79be:2384:cad7:d4c5'+'.json'
                            geo_req = requests.get(url)
                            print("GeoJS API Response:", geo_req.text)

                            geo_data = geo_req.json()
                            print("Geo Data:", geo_data)

                            city = geo_data['city']
                            country = geo_data['country']
                            speak(f"Sir, you are in {city} city of {country} country")
                        except Exception as e:
                            print("Error:", e)
                            speak("Sorry, I couldn't determine your location.")
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
                        shutdown = self.takeCommand().lower()
                        if "yes" in shutdown:
                            os.system("shutdown /s /t 1")
                        elif "no" in shutdown:
                            break

                    elif "exit" in query:
                        speak("Signing of Boss!")
                        exit()



startEcecution=mainFile()   



        
      

       


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=GuiofJarvis()
    ui.show()
    sys.exit(app.exec_())
