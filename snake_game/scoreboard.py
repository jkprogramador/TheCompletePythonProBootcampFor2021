from turtle import Turtle

FONT_PROPERTIES = ("Verdana", 12, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.__high_score = self.read_high_score()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.refresh()

    def increase_score(self):
        self.__score += 1
        self.refresh()

    @staticmethod
    def read_high_score() -> int:
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.__high_score))

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.__score} High Score: {self.__high_score}", align=ALIGN, font=FONT_PROPERTIES)

    def start_over(self):
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            self.write_high_score()

        self.__score = 0
        self.refresh()
