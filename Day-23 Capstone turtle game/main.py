from turtle import Turtle, Screen
from player import Player
import time
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
game_on = True
playerT = Player()
car = Car()
screen.listen()
screen.onkey(playerT.move, "Up")
score = Scoreboard()
while(game_on):
    time.sleep(0.1)
    screen.update()
    # time.sleep(1)
    car.create_car()
    # time.sleep(0)
    car.move()

    for i in car.all_cars:
        if i.distance(playerT) < 20:
            game_on = False
            score.game_over()

    if playerT.is_at_finish_l():
        playerT.go_to_s()
        car.level_up()
        score.level += 1
        score.update_s()




screen.exitonclick()