import turtle
mypen=turtle.Turtle()
mypen.shape('turtle')
mypen.speed(10)

window=turtle.Screen()
window.bgcolor('pink')



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
mypen.write("Mother's", font=style, align='center')
mypen.penup()
mypen.goto(0,-100)
mypen.write("Day", font=style,align='center')
mypen.penup()
mypen.goto(0,-150)
mypen.write("2021",font=style,align='center')
mypen.hideturtle()
turtle.done()