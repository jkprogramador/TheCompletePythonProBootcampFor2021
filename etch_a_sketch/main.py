import turtle


class Sketcher:
    def __init__(self):
        self.tim = turtle.Turtle()
        self.increment = 10

    def forward(self):
        self.tim.forward(self.increment)

    def backward(self):
        self.tim.back(self.increment)

    def counter_clockwise(self):
        self.tim.setheading(self.tim.heading() + self.increment)

    def clockwise(self):
        self.tim.setheading(self.tim.heading() - self.increment)

    def clear(self):
        self.tim.reset()


def main():
    screen = turtle.Screen()
    sketcher = Sketcher()
    screen.listen()
    screen.onkey(sketcher.forward, "w")
    screen.onkey(sketcher.backward, "s")
    screen.onkey(sketcher.clockwise, "d")
    screen.onkey(sketcher.counter_clockwise, "a")
    screen.onkey(sketcher.clear, "c")
    screen.exitonclick()


main()
