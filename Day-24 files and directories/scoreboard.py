from turtle import Turtle
from food import Food

ALLIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        # self.increment()
        self.score = 0
        with open("data.txt", 'r') as file:
            self.highscoree = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscoree}", False, ALLIGNMENT, FONT)

    def resett(self):
        if self.score > self.highscoree :
            self.highscoree = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscoree}")
        self.score = 0
        self.update_scoreboard()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, ALLIGNMENT, FONT)

    def increment(self):
        self.score += 1
        self.update_scoreboard()