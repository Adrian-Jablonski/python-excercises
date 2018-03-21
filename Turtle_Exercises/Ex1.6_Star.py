from turtle import *

shape("turtle")



def star():
    begin_fill()
    fillcolor("blue")
    for i in range(10):
        if i % 2 == 0:
            forward(50)
            right(144)
        else:
            forward(50)
            left(72)
    end_fill()

star()

up()
forward(100)
mainloop()