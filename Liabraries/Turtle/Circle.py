from turtle import *

tim = Turtle()
screen = Screen()

colormode(255)
tim.fillcolor((255, 0, 147))
tim.begin_fill()
count = 0
start = tim.pos()
while True:
    forward(count)
    left(360)
    count+=1
    if tim.pos == start:
        break

screen.exitonclick()
