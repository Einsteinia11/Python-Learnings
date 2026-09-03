# Python's turtle module is mainly for beginners and for anyone who wants to learn programming through visual, interactive drawing.

# Turtle is not normally used to build professional GUI applications or modern games. It's primarily an educational and creative-coding tool.

# Once you understand the concepts through Turtle, you can move toward things like Pygame for games, or Tkinter/PyQt for GUI applications.
from turtle import *

timmy = Turtle()
my_screen = Screen()
print(my_screen.canvheight)

#forwards the turtle 100 steps
# forward(100)
# #120 degree left (anti-clockwise)
# left(120)
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)

# # Hexagon
# left(60)
# forward(100)
# left(60)
# forward(100)
# left(60)
# forward(100)
# left(60)
# forward(100)
# left(60)
# forward(100)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)

# color('red')
# fillcolor('yellow') #"When I tell you to fill a shape, use yellow."
# begin_fill() #"Start recording the boundary of the shape. When I later call end_fill(), fill the enclosed area."
# start = pos() #position of the turtle right now

# while True:
#     forward(200)
#     left(170)
#     if distance(start) < 1: #If the turtle is less than 1 pixel away from the starting point... break
#         break
# end_fill()

# #8 petals flower
# start = pos()
# colormode(255) #Turtle expects RGB values between 0 and 1 by default, so (255, 0, 147) is invalid.
# fillcolor((9, 56, 4))
# begin_fill()
# while True:
#     forward(300)
#     left(160)
#     if distance(start) < 1:
#         break
# end_fill()

# #40 petals flower
# fillcolor((255, 0, 147))
# begin_fill()
# while True:
#     forward(300)
#     left(170)
#     if distance(start) < 1:
#         break
# end_fill()

# #Pentagon flower
# start = pos()
# fillcolor((255, 0, 147))
# begin_fill()
# while True:
#     right(90)
#     forward(300)
#     left(170)
#     if distance(start) < 1:
#         break
# end_fill()
# my_screen.exitonclick()