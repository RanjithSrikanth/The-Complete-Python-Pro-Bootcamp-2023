from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

for i in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)




screen = Screen()
screen.exitonclick()