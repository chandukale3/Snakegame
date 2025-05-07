from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Classic Snake Game ')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_over = False
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)
screen.onkey(key='Down', fun=snake.move_down)
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_scores()
        snake.reset_position()
    for tail in snake.my_turtles_list[1:]:
        if snake.head.distance(tail) < 10:
            scoreboard.reset_scores()
            snake.reset_position()


screen.exitonclick()