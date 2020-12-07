from turtle import Turtle

MOVEMENT_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, starting_position: tuple):
        super().__init__(shape="square")
        self.color("white")
        self.up()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT_DISTANCE)
