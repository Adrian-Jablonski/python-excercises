from shapes import *
from turtle import *

size = int(input("Enter the size of the shapes"))
fill = input("Fill shapes with a color? Type Yes to fill").capitalize()
if fill == "Yes":
    fill = True
else:
    fill = False
color = input("Enter pen color for shapes")

up()
left(180)
forward(150)
right(90)
forward(50)
down()

square(size, fill, color)

up()
right(90)
forward(30)
down()

equilateralTriangle(size, fill, color)

up()
forward(150)
down()

hexagon(size, fill, color)

up()
forward(180)
down()

star(size, fill, color)

up()
right(90)
forward(60)
right(90)
forward(125)
down()

octagon(size, fill, color)

up()
forward(155)
down()

circle1(size, fill, color)

up()
forward(100)
down()

pentagon(size, fill, color)

