import turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
MOVEMENT_DISTANCE = 20


class Snake:

    def __init__(self):
        self.__body = []
        self.create_body()
        self.__head = self.__body[0]

    def create_body(self):
        x = 0
        y = 0
        for _ in range(3):
            self.add_segment((x, y))
            x -= 20

    def add_segment(self, position: tuple):
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.up()
        segment.goto(position)
        self.__body.append(segment)

    def get_head(self) -> turtle.Turtle:
        return self.__head

    def get_body(self) -> list:
        return self.__body

    def right(self):
        if LEFT != self.__head.heading():
            self.__head.setheading(RIGHT)

    def up(self):
        if DOWN != self.__head.heading():
            self.__head.setheading(UP)

    def down(self):
        if UP != self.__head.heading():
            self.__head.setheading(DOWN)

    def left(self):
        if RIGHT != self.__head.heading():
            self.__head.setheading(LEFT)

    def move(self):
        for seg_num in range(len(self.__body) - 1, 0, -1):
            new_x = self.__body[seg_num - 1].xcor()
            new_y = self.__body[seg_num - 1].ycor()
            self.__body[seg_num].goto(new_x, new_y)

        self.__head.forward(MOVEMENT_DISTANCE)

    def extend(self):
        self.add_segment(self.__body[-1].position())

    def start_over(self):
        for segment in self.__body:
            segment.goto(1000, 100)

        self.__body.clear()
        self.create_body()
        self.__head = self.__body[0]
