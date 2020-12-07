import turtle
import paddle
import ball
import time
import scoreboard

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    right_paddle = paddle.Paddle((350, 0))
    left_paddle = paddle.Paddle((-350, 0))
    game_ball = ball.Ball((0, 0))
    score = scoreboard.Scoreboard()
    screen.listen()
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(right_paddle.move_down, "Down")
    screen.onkey(left_paddle.move_down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(game_ball.get_move_speed())
        screen.update()
        game_ball.move()

        # Detect collision of the ball with the top and bottom walls.
        if game_ball.ycor() > 280 or game_ball.ycor() < -280:
            game_ball.bounce_y()

        # Detect collision with both paddles.
        if (game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320) \
                or (game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320):
            game_ball.bounce_x()

        # Detect if right paddle misses.
        if game_ball.xcor() > 380:
            game_ball.restart()
            score.increase_left_score()

        # Detect if left paddle misses.
        if game_ball.xcor() < -380:
            game_ball.restart()
            score.increase_right_score()

    screen.exitonclick()


main()
