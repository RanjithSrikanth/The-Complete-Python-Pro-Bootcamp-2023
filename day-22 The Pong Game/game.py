from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.paddles = []
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(self.position)
        # self.paddles.append(pad1)

    def move_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def move_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)



