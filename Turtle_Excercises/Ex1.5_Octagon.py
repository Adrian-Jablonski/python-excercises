from turtle import *

shape("turtle")

def octagon():
    for i in range(8):
        forward(100)
        left(45)

octagon()
mainloop()