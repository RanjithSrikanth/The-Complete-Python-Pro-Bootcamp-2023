from turtle import Turtle, Screen
import random

colors = ['blue','pink','purple','red','green','yellow']

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

# for i in range(3):
#     timmy.forward(100)
#     timmy.right(120)
# timmy.color(random.choice(colors))
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for i in range(5):
#     timmy.forward(100)
#     timmy.right(72)
# for i in range(6):
#     timmy.forward(100)
#     timmy.right(60)
# for i in range(7):
#     timmy.forward(100)
#     timmy.right(51.42857142857143)
# for i in range(8):
#     timmy.forward(100)
#     timmy.right(45)
# for i in range(9):
#     timmy.forward(100)
#     timmy.right(40)
# for i in range(10):
#     timmy.forward(100)
#     timmy.right(36)

def turtlee(n):
    angle = 360 / n
    for i in range(n):
        timmy.forward(100)
        timmy.right(angle)

for i in range(3, 11):
    timmy.color(random.choice(colors))
    turtlee(i)

screen = Screen()
screen.exitonclick()