from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.setheading(90)
        self.up()
        self.restart()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def has_reached_finish_line(self) -> bool:
        return self.ycor() > FINISH_LINE_Y

    def restart(self):
        self.goto(STARTING_POSITION)
