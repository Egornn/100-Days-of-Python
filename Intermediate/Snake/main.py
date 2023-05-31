from turtle import Screen, Turtle
from random import randint
from time import sleep
from snake import Snake, GRID_SQUARE, GRID_SIZE


screen = Screen()
screen.setup(width=GRID_SIZE * GRID_SQUARE, height=GRID_SIZE * GRID_SQUARE)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)
snake_1 = Snake()
screen.listen()
screen.onkey(snake_1.move_up, 'Up')
screen.onkey(snake_1.move_down, 'Down')
screen.onkey(snake_1.move_left, 'Left')
screen.onkey(snake_1.move_right, 'Right')
while snake_1.is_continue:
    snake_1.move()
    screen.update()
    sleep(.3)
screen.exitonclick()
for s in snake_1.segments:
    print(s.pos())
