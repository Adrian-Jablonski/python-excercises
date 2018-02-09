from turtle import *

shape("turtle")

def moveIntoPosition():
    up()
    forward(50)
    left(90)
    forward(50)
    left(90)
    down()

def square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)

def circle1():
    pencolor("orange")
    width(10)
    circle(180)

def star():
    pencolor("blue")
    width(1)
    for i in range(5):
        forward(80)
        right(144)

moveIntoPosition()
square()

up()
forward(-120)
right(90)
forward(50)
down()

circle1()
up()
left(90)
forward(140)
left(20)
down()
star()

mainloop()