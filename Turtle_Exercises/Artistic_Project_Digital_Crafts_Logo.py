from turtle import *

shape("turtle")
bgcolor("black")
speed(9)

def trapezoid(color):
    begin_fill()
    pencolor(color)
    fillcolor(color)
    forward(100)
    right(120)
    forward(50)
    right(60)
    forward(50)
    right(60)
    forward(50)
    end_fill()

def equilateralTriangle(color, size):
    begin_fill()
    fillcolor(color)
    pencolor(color)
    for i in range(3):
        forward(size)
        left(120)   # 180 - angle of each side of triangle
    end_fill()

def parallelogram(color):
    begin_fill()
    fillcolor(color)
    pencolor(color)
    left(180)
    forward(50)
    right(120)
    forward(55) 
    right(60)
    forward(45)
    right(60)
    forward(5)
    end_fill()

def parallelogram2(color):
    begin_fill()
    fillcolor(color)
    pencolor(color)
    left(180)
    forward(50)
    left(60)
    forward(50)
    left(120)
    forward(55)
    left(60)
    forward(45)
    end_fill()

def parallelogram3(color):
    begin_fill()
    fillcolor(color)
    pencolor(color)
    forward(50)
    left(60)
    forward(50) 
    left(120)
    forward(55) 
    left(60)
    forward(45) 
    end_fill()

def parallelogram4(color):
    begin_fill()
    fillcolor(color)
    pencolor(color)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(55)
    right(60)
    forward(45)
    end_fill()

# get into position
up(); left(180); forward(100); right(90); forward(100); left(90); down()

#Top left
trapezoid("#55CC42")
equilateralTriangle("#72CF3D", 50)
parallelogram("#448F3D")

forward(-5)

equilateralTriangle("#2A7C66", 55)

forward(55)

# bottom left
equilateralTriangle("#0091D4", 50)

forward(50); right(60); forward(100); right(180)
trapezoid("#008AD0")

left(240); forward(150)

parallelogram2("#006ABB")

equilateralTriangle("#0062A6", 55)

forward(55)

equilateralTriangle("#0082B6", 55)

forward(55); left(180)
equilateralTriangle("#008AD0", 45)

up(); forward(55); left(60); forward(11); down()

equilateralTriangle("#A5AAAB", 45)

forward(45); left(60)
equilateralTriangle("#6E6E71", 55)

forward(55); left(60)

equilateralTriangle("#CC7F4B", 55)

forward(55); left(180)

equilateralTriangle("#FFB300", 50)

right(120)
# top right side
equilateralTriangle("#939597", 55)         

forward(50); left(180)

equilateralTriangle("#BBBDBF", 50)

left(60)
parallelogram3("#A5AAAB")

left(60); forward(5); left(60); forward(150); left(180)

trapezoid("#BBBDBF")

left(330)

up(); forward(87); right(90); forward(100); right(180); down()

trapezoid("#FF9C00")

left(60); up(); forward(50); left(180); down()

parallelogram4("#FF6D00")

speed(1)
color = "grey"
up(); left(60); fillcolor(color); pencolor(color)
color = "blue"
forward(350); right(90); fillcolor(color); pencolor(color); forward(50)
color = "green"
right(90); fillcolor(color); pencolor(color)

mainloop()