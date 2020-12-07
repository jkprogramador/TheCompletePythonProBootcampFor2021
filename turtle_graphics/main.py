import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")


def random_color():
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    tim.pencolor((random_red, random_green, random_blue))


# Draw a square.
def draw_square(side_length: int = 100):
    for _ in range(4):
        tim.forward(side_length)
        tim.right(90)


# draw_square()


# Draw a circle of squares
# for _ in range(60):
#     random_color()
#     draw_square()
#     tim.right(5)

# Draw a turtle spiral
# side_length = 5
# for _ in range(60):
#     draw_square(side_length)
#     side_length += 5
#     tim.right(5)

def draw_triangle(side_length: int = 100):
    for _ in range(3):
        tim.forward(side_length)
        tim.right(120)  # Get the external angle of triangle: 180 - 60


# draw_triangle()

# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.
# Each side must be 100 in length.
# Square: 90°.
# Pentagon: 72°.
# So divide 360° by the number of sides of the shape to get the right angle.
def draw_polygon(sides: int):
    angle = round(360 / sides, 2)

    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)


def draw_star(side_length: int = 100):
    """Draws five-point star."""
    for _ in range(5):
        tim.forward(side_length)
        tim.right(144)


# draw_star()
# starting_side_length = 100
# for _ in range(60):
#     random_color()
#     draw_star(starting_side_length)
#     starting_side_length += 5
#     tim.right(5)

# Draw a dashed line.
# for i in range(50):
#
#     if i % 2 == 0:
#         tim.down()
#     else:
#         tim.up()
#     tim.forward(5)


# def change_direction():
#     tim.setheading(random.choice([0, 90, 180, 270]))


# for i in range(3, 11):
#     random_color()
#     draw_polygon(i)


# tim.pensize(3)
#
# Draw random walk
# for _ in range(200):
#     tim.forward(15)
#     random_color()
#     change_direction()

# Draw circles
# for _ in range(0, 365, 5):
#     random_color()
#     tim.circle(100)
#     tim.setheading(_)

screen = turtle.Screen()
screen.exitonclick()
