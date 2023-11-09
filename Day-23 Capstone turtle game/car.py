from turtle import Turtle
import random
import time
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
MOVE_DISTANCE = 5
INCREMENT = 10

class Car:
    def __init__(self):
        self.all_cars = []
        self.move_s = MOVE_DISTANCE
    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for i in self.all_cars:
            i.setheading(180)
            i.forward(self.move_s)

    def level_up(self):
        self.move_s += INCREMENT



