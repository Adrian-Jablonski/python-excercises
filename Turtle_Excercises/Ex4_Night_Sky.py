from turtle import *
import random

starColors = ["#9bb0ff", "#aabfff", "#cad7ff", "#f8f7ff", "#fff4ea", "#ffd2a1", "#ffcc6f"]

x = -350
y = 300
i = 0

def randomVariables():
    global size
    global x
    global y
    global color
    goForward = random.randint(40, 65)
    size = random.randint(1, 5)
    if size < 2:
        z = random.randint(0, 3)
        color = starColors[z]
    elif size < 4:
        z = random.randint(2, 5)
        color = starColors[z]
    else:
        z = random.randint(4, 6)
        color = starColors[z]
    turn = random.randint(0, 15)
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)

bgcolor("black")
speed(0)
hideturtle()

randomVariables()

def star(size, color):
    begin_fill()
    fillcolor(color)
    pencolor(color)
    for i in range(10):
        if i % 2 == 0:
            forward(size)
            right(144)
        else:
            forward(size)
            left(72)
    end_fill()

while i < 200:
    up()
    if i % 25 == 0 and i != 0:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        duration = 0
        goForward = random.randint(20, 40)

        shootingStarX = random.randint(-20, 20)
        shootingStarY = random.randint(-20, 20)
        while duration <= 26:
            if duration <= 20:
                down()
                star(6, color)

            up()
            setpos(x, y)
            
            x += shootingStarX
            y += shootingStarY
            if duration > 2:
                down()
                pencolor("black")
                width(20)
                star(6, "black")
            #up()
            width(1)
            setpos((x + (shootingStarX * 6)), (y + (shootingStarY * 6)))
            duration += 1
            
    
    setpos(x, y)
    down()
    star(size, color)

    i += 1
    randomVariables()

mainloop()