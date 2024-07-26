from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
screen.listen()
screen.onkey(paddle.left_paddle_up, "Up")
screen.onkey(paddle.left_paddle_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)


screen.exitonclick()
