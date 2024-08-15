from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
LEFT_PADDLE_START_POS = (-350, 0)
RIGHT_PADDLE_START_POS = (350, 0)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

l_paddle = Paddle(LEFT_PADDLE_START_POS)
r_paddle = Paddle(RIGHT_PADDLE_START_POS)
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

ball = Ball()
# the ball by default has width and height of 20,20
# the ball by default starts at middle of the screen (0,0)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    # collision with the north and south walls
    if ball.ycor() >= 282 or ball.ycor() <= -280:
        ball.bounce_y()

    # collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # collision with west wall.
    if ball.xcor() > 380:
        scoreboard.r_point()
        BALL_SPEED = 0.1
        ball.reset()
    # collision with east wall.
    if ball.xcor() < -380:
        scoreboard.l_point()
        BALL_SPEED = 0.1
        ball.reset()

    screen.update()


screen.exitonclick()
