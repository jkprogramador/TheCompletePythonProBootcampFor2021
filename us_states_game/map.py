import turtle


class Map(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()

    def draw_text(self, text: str, coordinates: tuple):
        self.goto(coordinates)
        self.write(arg=text, align="center", font=("Arial", 10, "normal"))
