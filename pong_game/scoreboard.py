from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.hideturtle()
        self.__left_score = 0
        self.__right_score = 0
        self.__update_score()

    def __update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.__left_score, align="center", font=("Courier New", 80, "normal"))
        self.goto(100, 200)
        self.write(self.__right_score, align="center", font=("Courier New", 80, "normal"))

    def increase_left_score(self):
        self.__left_score += 1
        self.__update_score()

    def increase_right_score(self):
        self.__right_score += 1
        self.__update_score()
