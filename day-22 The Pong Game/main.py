from turtle import Screen
from game import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.title("The Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()
game_on = True

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) > 50 and ball.ycor() < -340:
        ball.bounce_x()

    #detect right paddle misses
    if ball.xcor() > 380 :
        ball.reset_p()
        score.l_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_p()
        score.r_point()



screen.exitonclick()