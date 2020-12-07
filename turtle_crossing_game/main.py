import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

the_player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(the_player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect collision with cars.
    for car in cars.get_cars():
        if car.distance(the_player) < 20:
            score.game_over()
            game_is_on = False

    # Detect when the player has reached the top edge of the screen.
    if the_player.has_reached_finish_line():
        the_player.restart()
        cars.increase_speed()
        score.increase_level()

screen.exitonclick()
