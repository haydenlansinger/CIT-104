# ------------------------------
# Name: circle.py
# Author: Hayden Lansinger
# Date: 10/28/2026
# Description: This program will exercise Turtle graphics to draw a circle.
# ------------------------------

from turtle import Turtle
import math
t = Turtle()

def drawCircle(turtle, centerX, centerY, radius):
    # sets up the turtle to create the circle
    turtle.penup()
    turtle.goto(centerX, centerY)
    turtle.forward(radius)
    turtle.setheading(-90)
    turtle.pendown()

    # draws the cirlce
    for turn in range(120):
        turtle.right(3)
        turtle.forward(2.0 * math.pi * radius / 120.0)

# a simple function call
drawCircle(t, 14, 26, 116)
input("Press ENTER to exit.")


