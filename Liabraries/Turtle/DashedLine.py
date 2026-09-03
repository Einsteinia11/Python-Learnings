from turtle import *

tim = Turtle()
screen = Screen()

for i in range(1, 40):
    if i%2==0:
        tim.pendown()
        tim.forward(10)
    else:
        tim.penup()
        tim.forward(10)
screen.exitonclick()