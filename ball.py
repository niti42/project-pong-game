from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ydirection = random.choice([1, -1])
        self.xdirection = 1
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xdirection*10
        new_y = self.ycor() + self.ydirection*10
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ydirection = -self.ydirection

    def bounce_x(self):
        self.xdirection = -self.xdirection
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
        self.ydirection = random.choice([1, -1])
