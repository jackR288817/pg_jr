import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch ("SAPI.SpVoice")

r = sr.Recognizer ()

with sr.Microphone()as source:
    speak.Speak("hello leader, what should I do for you")
    print ("shut up")

    audio = r.listen(source)
    print ("stop talking")

try:
    words = r.recognize_google (audio)
    speak.Speak ("ok,lets look.")
    wb.open ("https://www.youtube.com/results?search_query=" + words)

except sr.UnknownValueError:
    print("google Speach Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognitionservice;")
