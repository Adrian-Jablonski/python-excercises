from turtle import *

shape("turtle")

def equilateralTriangle(size=110, fill=True, color="black"):
    
    if fill == True:
        begin_fill()
        fillcolor("red")
    pencolor(color)
    for i in range(3):
        forward(size)
        left(120)   # 180 - angle of each side of triangle
    end_fill()

def square(size=100, fill=True, color="black"):
    
    if fill == True:
        begin_fill()
        fillcolor("yellow")
    pencolor(color)
    for i in range(4):
        forward(size)
        left(90)
    end_fill()

def pentagon(size=65, fill=True, color="black"):
    
    if fill == True:
        begin_fill()
        fillcolor("grey")
    pencolor(color)
    for i in range(5):
        forward(size)
        left(72)
    end_fill()
    mainloop()

def hexagon(size=60, fill=True, color="black"):
    
    if fill == True:
        begin_fill()
        fillcolor("green")
    pencolor(color)
    for i in range(6):
        forward(size)
        left(60)
    end_fill()
    
def octagon(size=40, fill=True, color="black"):
    
    if fill == True:
        begin_fill()
        fillcolor("black")
    pencolor(color)
    for i in range(8):
        forward(size)
        left(45)
    end_fill()

def star(size=50, fill=True, color="black"):
    
    if fill == True:
        begin_fill()
        fillcolor("blue")
    pencolor(color)
    for i in range(10):
        if i % 2 == 0:
            forward(size)
            right(144)
        else:
            forward(size)
            left(72)
    end_fill()

def circle1(size=50, fill=True, color="black"):
    if fill == True:
        begin_fill()
        fillcolor("orange")
    pencolor(color)
    circle(size)
    end_fill()
