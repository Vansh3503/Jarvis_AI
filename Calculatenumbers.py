import wolframalpha
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wolframalpha(query):
    apikey = "E46TV4-3K25R9PHH2"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = Wolframalpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
