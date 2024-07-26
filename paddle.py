from turtle import Turtle
# create left paddle
# create right paddle
MOVE_DSTANCE = 20
UP = 90
DOWN = 270


LEFT_PADDLE_START_POS = [
    (-350, -40), (-350, -20), (-350, 0), (-350, 20), (-350, 40)]
RIGHT_PADDLE_START_POS = [
    (350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]


class Paddle():
    def __init__(self) -> None:
        self.left_paddle_segments = []
        self.right_paddle_segments = []
        self.create_left_paddle()
        self.create_right_paddle()

    def create_left_paddle(self):
        for position in LEFT_PADDLE_START_POS:
            self.add_segment(position, self.left_paddle_segments)

    def create_right_paddle(self):
        for position in RIGHT_PADDLE_START_POS:
            self.add_segment(position, self.right_paddle_segments)

    def add_segment(self, position, paddle_segments):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        paddle_segments.append(new_segment)

    def left_paddle_up(self):
        self.left_paddle_segments[-1].setheading(UP)
        for seg_num in range(len(self.left_paddle_segments)-1):
            self.left_paddle_segments[seg_num].goto(
                self.left_paddle_segments[seg_num+1].pos())
        self.left_paddle_segments[-1].forward(MOVE_DSTANCE)

    def left_paddle_down(self):
        self.left_paddle_segments[0].setheading(DOWN)
        for seg_num in range(len(self.left_paddle_segments)-1, 0, -1):
            self.left_paddle_segments[seg_num].goto(
                self.left_paddle_segments[seg_num-1].pos())
        self.left_paddle_segments[0].forward(MOVE_DSTANCE)
