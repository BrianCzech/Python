from audioop import add
from urllib import request
import newsapi
import pyttsx3 #pip install pyttsx3== text data into speech 
import datetime
import speech_recognition as sr #pip install SpeechRecognition==speech from mic to text format
import smtplib
#from secrets import senderemail, epwd, to 
from email.message import EmailMessage, Message
import pyautogui
import webbrowser as wb
from time import sleep, time
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
from wikipedia.wikipedia import languages, search
import clipboard
import os
import pyjokes
import time as tt
import string
import random
from PyDictionary import PyDictionary 



engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices=engine.getProperty('voices')
    #print(voices[0].id)
    if voice ==1:
        engine.setProperty('voice',voices[0].id)
        speak('Hello, this is Jarvis')  
    if voice ==2:
        engine.setProperty('voice',voices[1].id) 
        speak('Hello, this is Friday')  
    

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") # hour =I minutes =M seconds =S
    speak('The current time is:')
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(month)
    speak(date)
    speak(year)

def greeting():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Morning Sir')
    elif hour >=12 and hour <18:
        speak('Good afternoon Sir')
    elif hour >18 and hour <24:
        speak('Good evening Sir')
    else:
        speak('Good night sir')

def wishme():
    speak('Welcome back sir!')
    time()
    date()
    greeting()
    speak('Jarvis at your service, please tell me how can I help you?')

#while True:
    #voice=int(input("Press 1 for male voice\nPress 2 for female voice\n"))
    #speak(audio) 
    #getvoices(voice)
#wishme()

def takeCommandCMD():
    query=input('please tell me how can I help you?')
    return query

def takeCommandMic():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio =r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again please...')
        return 'None'
    return query

#News (Works)
def news():
    newsapi=NewsApiClient(api_key='1c814ddfb29f4120bc5d67af3f8fd5aa')
    speak('what topic you need the news about ?')
    topic=takeCommandMic()
    data=newsapi.get_top_headlines(q=topic,
                                   language='en',
                                   page_size=5)
    newsdata=data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("that's it for now. I'll update you in some time")


#Send Email (Doesn't Work)
def sendEmail(receiver,subject,content):
    server=smtplib.SMTP('smtpauth.mail.wowway.com', 25)
    server.starttls()
    server.login(senderemail, epwd)
    email=EmailMessage()
    email['From']=senderemail
    email['To']=receiver
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email)
    server.close()

#WhatsApp (Works)
def sendwhatsmsg(phone_number,message):
    Message=message
    wb.open('https://web.whatsapp.com/send?phone='+phone_number+'&text'+Message)
    sleep(10)
    pyautogui.press('enter')

#Google (Works)
def searchgoogle():
    speak('what should I search for ?')
    search=takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


#Text2Speech (Doesn't Work Correctly)
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

#Covid Cases (Works)
def covid():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    covid_data=f'Confirm cases: {data["cases"]} \n Deaths: {data["deaths"]} \n Recovered: {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

#Take a Screenshot (Works)
def screenshot():
    name_img=tt.time()
    name_img=f'C:\\Users\\brcze\\OneDrive\\Pictures\\Screenshots\\{name_img}.png'
    img=pyautogui.screenshot(name_img)
    img.show()

#Create Random Password (Works)
def passwordgen():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation

    passlen=8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass=("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

#Define a coin flip (Works)
def flip():
    speak('okay sir, flipping a coin')
    coin=['heads','tails']
    toss=[]
    toss.extend(coin)
    random.shuffle(toss)
    toss=("".join(toss[0]))
    speak("I flipped the coin and you got " +toss)

#Rolling a Die (Works)
def dice():
    speak('okay sir, rolling a die for you')
    die=['1','2','3','4','5','6']
    dice=[]
    dice.extend(die)
    random.shuffle(dice)
    dice=("".join(dice[0]))
    speak('I rolled a die and you got '+dice)

#Dictionary (Works)
def dictionary():
    speak('What word do you want to know ?')
    dictn=takeCommandMic()
    dictionary=PyDictionary()
    print(dictionary.meaning(dictn))
    speak(dictionary.meaning(dictn))







#Main Program
if __name__=='__main__':
    getvoices(1)
    #wishme()
    while True:
        query=takeCommandMic().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        #Email (Not Working Properly)
        elif 'email' in query:
            email_list={
                'Email':'brczech@wowway.com'
            }
            try:
                speak('To whom you want to send the mail ?')
                name=takeCommandMic()
                receiver=email_list[name]
                speak('what is the subject of the mail?')
                subject=takeCommandMic()
                speak('what should I say?')
                content=takeCommandMic()
                sendEmail(receiver,subject,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Unable to send the email')

        #Whats App (Works Kinda)
        elif 'message' in query:
            user_name={
                'Jarvis':'+1(586)925-7999'
            }
            try:
                speak('To whom you want to send the whats app message ?')
                name=takeCommandMic()
                phone_number=user_name[name]
                speak('what is the message?')
                message=takeCommandMic()
                sendwhatsmsg(phone_number,message)
                speak('message has been sent')
            except Exception as e:
                print(e)
                speak('Unable to send the message')

        #Wikipedia (works)
        elif 'wikipedia' in query:
            speak ('searching on wikipedia...')
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        #Google (Works)
        elif 'search' or 'Google' in query:
            searchgoogle()
        
        #Youtube
        elif 'youtube'in query:
            speak('what should I search for on youtube?')
            topic=takeCommandMic()
            pywhatkit.playonyt(topic)
        
        #Weather (Works)
        elif 'weather' in  query:
            city='clinton township'
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=f8adff8e01db570e0de78fc9a5164661'
            res=requests.get(url)
            data=res.json()
            weather=data['weather'][0]['main']
            temp=data['main']['temp']
            desp=data['weather'][0]['description']
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is like')
            speak('Temperature: {} degrees fahrenheit'.format(temp))
            speak('weather is {}'.format(desp))

        #News (Works)
        elif 'news' in query:
            news()

        #Text2Speech (Doesn't Work Correctly)
        elif 'read' in query:
            text2speech()
        
        #Covid (Works)
        elif 'covid' in query:
            covid()

        #Open VS Code (Works)
        elif 'open code' in query:
            codepath='C:\\Users\\brcze\\Downloads\\VSCodeUserSetup-x64-1.49.0.exe'
            os.startfile(codepath)


        #Open My Documents (Works)
        elif 'open documents' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        #Tell Programming Jokes (Works)
        elif 'joke' in query:
            speak(pyjokes.get_joke(language='en', category='all'))
        
        #Create Screenshot (Works)
        elif 'screenshot' in query:
            screenshot()

        #Tell System to Remember something (Works)
        elif 'remember that' in query:
            speak('what should i remember ?')
            data=takeCommandMic()
            speak('you said to remember that'+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        
        #Repeating what needs to be Remembered (Works)
        elif 'Tell me what I need to remember' in query:
            remember =open('data.txt', 'r')
            speak('you told me to remember that '+remember.read())

        ##Create Random Password (Works)
        elif 'password' in query:
            passwordgen()
        
        #Flip a Coin (Works)
        elif 'flip' in query:
            flip()

        #Rolling a Die (Works)
        elif 'dice' in query:
            dice()

        #Dictionary (Works)
        elif 'dictionary' in query:
            dictionary()


        #Go Offline (Works)
        elif 'offline' or 'shut down' or 'turn off'  or 'goodbye' in query:
            quit()


