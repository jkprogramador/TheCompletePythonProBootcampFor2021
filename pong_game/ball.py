from turtle import Turtle

MOVEMENT_DISTANCE = 10


class Ball(Turtle):
    def __init__(self, starting_position: tuple):
        super().__init__(shape="circle")
        self.__x_move = MOVEMENT_DISTANCE
        self.__y_move = MOVEMENT_DISTANCE
        self.color("white")
        self.up()
        self.goto(starting_position)
        self.__move_speed = 0.1

    def get_move_speed(self) -> float:
        return self.__move_speed

    def move(self):
        self.goto(self.xcor() + self.__x_move, self.ycor() + self.__y_move)

    def bounce_y(self):
        self.__y_move *= -1

    def bounce_x(self):
        self.__x_move *= -1
        self.__move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.__move_speed = 0.1
        self.bounce_x()
