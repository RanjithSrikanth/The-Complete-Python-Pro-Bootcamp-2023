from turtle import Turtle
from food import Food

SPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVED = 20 #MOVE DISTANCE
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180



class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for i in SPOSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        turtle = Turtle(shape='square')
        turtle.penup()
        turtle.color('white')
        turtle.goto(position)
        self.turtles.append(turtle)

    def resett(self):
        for i in self.turtles:
            i.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()


    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            xc = self.turtles[i - 1].xcor()
            yc = self.turtles[i - 1].ycor()
            self.turtles[i].goto(xc, yc)
        self.turtles[0].forward(MOVED)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)
