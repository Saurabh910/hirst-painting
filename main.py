import turtle
from turtle import Turtle
import random

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.penup()
tim.sety(-185)
tim.speed("fastest")

for y in range(10):
    tim.setx(-185)
    for x in range(10):
        tim.pendown()
        next_color = random_color()
        tim.dot(20, next_color)
        tim.penup()
        tim.forward(30)
        tim.setx(tim.xcor() + 50)
    tim.sety(tim.ycor() + 50)

screen = turtle.Screen()
screen.exitonclick()