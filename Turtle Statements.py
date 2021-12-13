import turtle
mypen=turtle.Turtle()

import pyttsx3
import speech_recognition

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices=engine.getProperty('voices')




mypen.shape('turtle')
mypen.speed(10)

window=turtle.Screen()
window.title("Dad's Birthday")
window.bgcolor('purple')



style=('Courier',50,'italic')
rainbow=['red','orange','yellow','green','blue','indigo','violet']
size=200

mypen.penup()
mypen.goto(0,80)
for color in rainbow:
    mypen.color(color)
    mypen.fillcolor(color)
    mypen.begin_fill()
    mypen.circle(size)
    size=-30

mypen.penup()
mypen.color('skyblue')
mypen.goto(0,-0)
mypen.write("Happy", font=style, align='center')
mypen.penup()
mypen.goto(0,-50)
mypen.write("Birthday", font=style, align='center')
mypen.penup()
mypen.goto(0,-100)
mypen.write("Dad", font=style,align='center')

mypen.hideturtle()

speak("Happy Birthday Dad. You're the best")

turtle.done()


