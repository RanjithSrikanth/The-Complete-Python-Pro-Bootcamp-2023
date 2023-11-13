from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score_board

tim = Turtle()
tim.write("Score : ", False, "center", font=("Arial", 8, "normal"))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboardd = Score_board()
game_on = True

# food_h = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboardd.increment()
    x = snake.turtles[0].xcor()
    y = snake.turtles[0].ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        scoreboardd.resett()
        snake.resett()
    for i in snake.turtles[1:]:
        if snake.turtles[0].distance(i) < 15:
            scoreboardd.resett()
            snake.resett()
    # if snake.turtles[0]

screen.exitonclick()