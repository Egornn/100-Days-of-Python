from turtle import Screen
from food import  Food
from time import sleep
from snake import Snake, GRID_SQUARE, GRID_SIZE
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=GRID_SIZE * GRID_SQUARE, height=GRID_SIZE * GRID_SQUARE)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)
snake_1 = Snake()
food_tile = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake_1.move_up, 'Up')
screen.onkey(snake_1.move_down, 'Down')
screen.onkey(snake_1.move_left, 'Left')
screen.onkey(snake_1.move_right, 'Right')
while snake_1.is_continue:
    screen.update()
    sleep(.1)
    snake_1.move()

    if food_tile.distance(snake_1.segments[-1]) < GRID_SQUARE/2:
        while snake_1.is_overlap(food_tile.pos()):
            food_tile.refresh()
        snake_1.extend()
        score_board.increase()

score_board.game_over()
screen.exitonclick()
