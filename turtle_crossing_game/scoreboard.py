from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__level = 1
        self.hideturtle()
        self.color("black")
        self.goto(-280, 250)
        self.refresh()

    def increase_level(self):
        self.__level += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Level: {self.__level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
