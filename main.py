from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Baby's First Video Game 🐍")
screen.tracer(0, 0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True


def game_end():
    scoreboard.reset_game()
    snake.reset_snake()


def game_closed():
    global game_is_on
    game_is_on = False
    food.remove_food()
    snake.remove_snake()
    screen.update()
    scoreboard.game_closed()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(game_closed, "Escape")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move_food()
        snake.grow_snake()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_end()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_end()

screen.exitonclick()
