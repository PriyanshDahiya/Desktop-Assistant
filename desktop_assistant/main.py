#imports
import datetime
import os
import smtplib
import sys
import webbrowser
import pyttsx3
import pywhatkit
import random
import speech_recognition as sr
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
hour = int(datetime.datetime.now().hour)

def talk(text):
    engine.say(text)
    engine.runAndWait()

greetings = ['hello sir', 'hi sir', 'howdy master']
decline = ['sorry, you are not authorized in this system', 'sorry, the password is incorrect']
value = random.choice(decline)
talk("Before proceeding, please say the password.")
with sr.Microphone() as source:
    print('Listening...')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    print(command)
if "start" not in command:
    talk(value)
    sys.exit()

talk("Hello sir. Allow me to introduce myself. I am Jarvis, a virtual artificial intelligence. "
     "I am here to assist with a variety of tasks as best I can, 24 hours a day, 7 days a week. "
     "Systems are now fully operational. Please tell me, what can I do for you?")

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dpriyansh23@gmail.com', 'wdmezqbcaunlyhbw')
    server.sendmail('dpriyansh23@gmail.com', to, content)
    server.close()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

    except:
        pass
    return command

def run_jarvis():
     command = take_command()
     print(command)
     if 'play' in command:
         song = command.replace('play','')
         talk('Playing'+ song)
         pywhatkit.playonyt(song)
     elif 'hello jarvis' in command:
         say = random.choice(greetings)
         talk(say)
     elif 'command prompt' in command or 'c m d' in command:
         talk("Launching command prompt")
         os.system('start cmd')
     elif 'google' in command:
         talk("Sir, what should I search on Google?")
         cm = take_command().lower()
         webbrowser.open_new(f'https://www.google.com/search?q={cm}')
     elif 'send an email' in command or 'send email' in command:
         try:
             talk("To whom should I send the email?")
             order = take_command().lower()
             if 'myself' in order or 'priyansh' in order:
                 talk("What should I say?")
                 content = take_command().lower()
                 to = "dpriyansh23@gmail.com"
                 send_email(to, content)
                 talk("Email has been sent to Priyansh")
             else:
                 talk("Sorry sir, there is no such contact.")
         except Exception as e:
             print(e)
     elif 'instagram' in command:
         talk("Launching Instagram")
         webbrowser.open_new("https://www.instagram.com")
     elif 'time' in command:
         time = datetime.datetime.now().strftime("%I:%M %p")
         print(time)
         talk("current time is"+ time)
     elif 'what' in command:
         talk("searching on wikipedia")
         persion1 = command.replace("what", "")
         info1 = wikipedia.summary(persion1, 1)
         print(info1)
         talk(info1)
     elif 'by' or 'bye' or 'goodbye' in command:
         sys.exit()
     else:
         talk("sorry sir, can you say that again?")
while True:
    run_jarvis()