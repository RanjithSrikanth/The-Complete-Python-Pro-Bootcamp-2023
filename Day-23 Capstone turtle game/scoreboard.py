from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-285, 275)
        self.update_s()

    def update_s(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 15, "normal"))


