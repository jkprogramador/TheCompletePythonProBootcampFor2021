import turtle
import random


class RacingTurtle:
    def __init__(self, color: str):
        self.turtle = turtle.Turtle(shape="turtle")
        self.turtle.color(color)

    def set_position(self, x: float, y: float):
        self.turtle.up()
        self.turtle.goto(x=x, y=y)

    def race(self, distance: int):
        self.turtle.forward(distance)

    def get_x(self) -> float:
        return self.turtle.xcor()

    def get_color(self) -> str:
        return self.turtle.pencolor()


def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
    colors = ["purple", "blue", "green", "yellow", "orange", "red"]
    number_of_participants = 6
    participants = []
    starting_x = -230
    starting_y = 150

    for i in range(number_of_participants):
        racing_turtle = RacingTurtle(color=colors[i])
        racing_turtle.set_position(x=starting_x, y=starting_y)
        participants.append(racing_turtle)
        starting_y -= 50

    is_race_on = False

    if user_bet:
        is_race_on = True

    while is_race_on:
        for participant in participants:

            if participant.get_x() > 230:
                is_race_on = False
                winning_color = participant.get_color()

                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost. The {winning_color} turtle is the winner.")

            random_distance = random.randint(0, 10)
            participant.race(random_distance)

    screen.exitonclick()


main()
