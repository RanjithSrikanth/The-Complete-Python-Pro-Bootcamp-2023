from turtle import Turtle

STARTING_P = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.go_to_s()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_s(self):
        self.goto(STARTING_P)

    def is_at_finish_l(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False