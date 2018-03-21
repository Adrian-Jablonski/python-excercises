from turtle import *

shape("turtle")

def hexagon():
    for i in range(6):
        forward(100)
        left(60)

hexagon()
mainloop()