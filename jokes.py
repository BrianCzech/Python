import requests 
import json

import pyttsx3 #pip install pyttsx3== text data into speech 

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

url="https://official-joke-api.appspot.com/jokes/random"

data=requests.get(url)
random_joke=json.loads(data.text)

print(random_joke["setup"])
print(random_joke['punchline'])

speak(random_joke["setup"])
speak(random_joke['punchline'])