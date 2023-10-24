import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
# colors = ['blue', 'pink', 'purple', 'red', 'green', 'yellow']
directions = [0, 90, 180, 270]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ctuple = (r, g, b)
    return ctuple

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pensize(15)
timmy.speed('fastest')
for i in range(100):
    color = random_color()
    timmy.color(color)
    timmy.setheading(random.choice(directions))
    timmy.forward(40)


screen = Screen()
screen.exitonclick()
