import turtle
import snake
import time
import food
import scoreboard


def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    game_snake = snake.Snake()
    snake_food = food.Food()
    score = scoreboard.Scoreboard()
    screen.listen()
    screen.onkey(game_snake.right, "Right")
    screen.onkey(game_snake.up, "Up")
    screen.onkey(game_snake.down, "Down")
    screen.onkey(game_snake.left, "Left")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        game_snake.move()

        # Detect collision with food.
        if game_snake.get_head().distance(snake_food) < 15:
            # Food should go to random location.
            snake_food.refresh()
            # Extend the snake itself.
            game_snake.extend()
            # Increase the score.
            score.increase_score()

        # Detect collision with wall.
        if game_snake.get_head().xcor() > 280 or \
                game_snake.get_head().xcor() < -280 or \
                game_snake.get_head().ycor() > 280 or \
                game_snake.get_head().ycor() < -280:
            score.start_over()
            game_snake.start_over()

        # Detect collision with tail.
        # If the head collides with any segment in the tail, game over:
        for segment in game_snake.get_body()[1:]:
            if game_snake.get_head().distance(segment) < 10:
                score.start_over()
                game_snake.start_over()

    screen.exitonclick()


main()
