import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.__cars = []
        self.create_car()
        self.__move_speed = STARTING_MOVE_DISTANCE

    def get_cars(self) -> list:
        return self.__cars

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            car = turtle.Turtle(shape="square")
            car.up()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, random.randint(-250, 250))
            self.__cars.append(car)

    def move_cars(self):
        for car in self.__cars:
            car.backward(self.__move_speed)

    def increase_speed(self):
        self.__move_speed += MOVE_INCREMENT
