# import colorgram
#
# colors = colorgram.extract("hirst.jpg", 54)
#
# rgb_colors = []
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(rgb_colors)
import turtle
import random

turtle.colormode(255)

colors = [
    (230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18),
    (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23),
    (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170),
    (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90),
    (18, 75, 105), (91, 153, 156), (45, 49, 45), (104, 52, 26), (161, 202, 213), (213, 203, 31)
]


def random_color() -> tuple:
    return random.choice(colors)


timmy = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(1920, 1080)
timmy.shape("turtle")
timmy.speed("fastest")
screen_size = screen.screensize()
width = screen_size[0]
height = screen_size[1]

# Print 10x10 dots.
# Each dot has radius 10, with 50 spaces separating each dot.
# radius = 10
spacing = 50
angle = -90
timmy.up()
timmy.setpos(-width / 2 + 50, height / 2 - 50)
timmy.down()

timmy.up()
for i in range(10):
    angle *= -1
    # radius *= -1
    for j in range(10):
        timmy.dot(20, random_color())
        # timmy.color(random_color())
        # timmy.begin_fill()
        # timmy.circle(radius)
        # timmy.end_fill()
        # timmy.up()
        timmy.forward(spacing)
        # timmy.down()

    # timmy.up()
    timmy.back(spacing)
    timmy.right(angle)
    timmy.forward(spacing)
    timmy.right(angle)
    # timmy.down()

screen.exitonclick()
