import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib 
import random
from plyer import notification
from googlesearch import search 
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir ' krishna artificial intellegnce. Please tell me how may I help you ")


def water():
    notification.notify(
        title="JA JAKE PANI PIKE AA",
        message='''Since your brain is mostly water, drinking it helps you in a number of ways,
        including: Improving concentration and cognition. Helping to balance your mood and emotions.
        Maintaining memory function.''',
        app_icon=r"D:\HELLO WORLD\Julie-Henriksen-Kitchen-Water-Boiler-Electric-Kettle.ico",
        timeout=12    )

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(
        'krishnamaheshwari@myserver.com', 'krishna')
    server.sendmail('krishnamaheshwari249@gmail.com', to, content)
    server.close()

while True:
    method = input('Choose your preffered commanding method(speak/write) : ')
    if method.lower() == 'speak':
        break
    elif method.lower() == 'write':
        break
    else:
        print('Please enter a valid method')

def takeCommand():
    if method == 'speak':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as _:
            print("Say that again please...")
            return "None"
    else:
        query = input('Enter the command : ')
    return query

webbrowser.register('Brave',None,webbrowser.BackgroundBrowser(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"))
while True:
    query = takeCommand().lower()
    
    if 'search' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.get('Brave').open('http://youtube.com')

    elif 'play gayatri mantra' in query:
        webbrowser.get('Brave').open('https://youtube.com/watch?v=iwpCHfj47CA')

    elif 'open google' in query:
        webbrowser.get('Brave').open('http://google.com')

    elif 'open stackoverflow' in query:
        webbrowser.get('Brave').open('http://stackoverflow.com')

    elif 'find about' in query:
        query1 = query.replace('find about',' ')
        for i in search(query1,num=5,stop=10):
            webbrowser.get('Brave').open_new_tab(i)
            
            
    elif 'play song' in query:
            query = query.replace('play song','spotify')
            for i in search(query,num=1,stop=1):
                webbrowser.get('Brave').open(i)


    elif 'youtube' in query:
        for i in search(query,num=5,stop=1):           
            webbrowser.get('Brave').open(i)

    elif 'i am feeling low' in query:
        webbrowser.get('Brave').open('https://www.youtube.com/watch?v=WJTd1iSch94&t=242s')

    elif 'wish happy birthday to' in query:
        query = query.replace('wish','')
        query = query.replace('to','')
        speak (query)
    elif 'open whatsapp' in query:
        webbrowser.get('Brave').open('https://web.whatsapp.com')

    elif 'open telegram' in query:
        webbrowser.get('Brave').open('https://web.telegram.com')             
    
    elif 'open quora'  in query :
        webbrowser.get('Brave').open('https://quora.com')

    elif 'open instagram' in query :
        webbrowser.get('Brave').open('https://instagram.com')

    elif 'spiritual time' in query :
        webbrowser.get('Brave').open('https://isha.sadhguru.org/mahashivratri/shiva-adiyogi/shiva-tanda')
        
    elif 'introduce yourself' in query :
        wishMe()

    elif 'play chess' in query:
        webbrowser.get('Brave').open('https://chess.com')

    elif 'play music' in query:
        music_dir = 'I:\\ritviz'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'play movies' in query:
        movies_dir = r"H:\\movies"
        movies = os.listdir(movies_dir)
        movie = random.choices(movies)[0]
        os.startfile(os.path.join(
            movies_dir, movies[movies.index(movie)]))
        speak(f"Ok krishna ,playing {movie}")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = 'C:\\Users\\krish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codePath)
    
    elif 'today is my birthday' in query :
        speak("happy birthday sir ")

    elif 'email to krishna' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "krishnamaheshwari256@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as _:
            print(_)
            speak("Sorry my friend bhai. I am not able to send this email")

    elif 'open input box' in query:
        a = input()

    elif 'open chrome' in query:
        chromePath = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
        os.startfile(chromePath)

    elif 'open spotify' in query:
        spotifyPath = 'C:\\Users\\krish\\AppData\\Roaming\\Spotify\\Spotify.exe'
        os.startfile(spotifyPath)
        
    elif 'play' in query:
        pyautogui.press('playpause')

    elif 'take me to the ebook store' in query:
        webbrowser.get('Brave').open('https://www.pdfdrive.com/')

    elif  'open classroom'  in query:
        webbrowser.get('Brave').open('https://classroom.google.com/u/1/h')

    elif 'increase the volume' in query:
        pyautogui.press('volumeup')

    elif 'volume down' in query:
        pyautogui.press ('volumedown')

    elif 'next song' in query :
        pyautogui.press ('nexttrack')

    elif 'previous song' in query :
        pyautogui.press ('prevtrack')  

    elif 'what can you do' in query:
        helpPath = '"D:\\HELLO WORLD\\ai\\help.txt"'
        os.startfile(helpPath)
    elif 'Add a new application' in query:
        app_no = int(1)
        app_name = input('Please tell the name of this app')
        app_location = input('Please tell the location of this app and add a \\ before every \\')
        app_command = input('Please tell how you wish me to open this app')
        app_no_new = app_no + 1


    elif app_name in query:
        appPath = app_location
        os.startfile(appPath)

        
    elif 'leave' in query:
        break



    else:
        print('Sorry,I can not help with you that')


    