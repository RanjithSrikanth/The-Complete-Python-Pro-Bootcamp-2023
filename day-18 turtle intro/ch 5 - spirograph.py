import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ctuple = (r, g, b)
    return ctuple


for i in range(50):
    head = timmy.heading()
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(head + 10)


screen = t.Screen()
screen.exitonclick()