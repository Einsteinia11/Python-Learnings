from turtle import *

tim = Turtle()
screen = Screen()

colormode(255)
tim.fillcolor((255, 0, 147))
tim.begin_fill()
tim.forward(200)
tim.left(120)
tim.forward(200)
tim.left(120)
tim.forward(200)
tim.left(120)
tim.end_fill()

screen.exitonclick()
