from turtle import Screen, Turtle
from random import randint


def add_turtle(x: int, y:int, snake_list= []):
    new_turtle = Turtle(shape='square', visible=False)
    new_turtle.penup()
    new_turtle.color('white')
    new_turtle.setposition(x * GRID_SQARE, y*GRID_SQARE)
    new_turtle.showturtle()
    snake_list.append(new_turtle)
    return snake_list


def initial_setup():
    initial_coordinates = [(-2, 0), (-1, 0), (0, 0)]
    for coordinates in initial_coordinates:
        snake = add_turtle(coordinates[0], coordinates[1])
    head = snake.pop(-1)
    is_continue = True
    while is_continue:
        screen.delay(100)
        snake.append(head)
        new_x = head.xcor() + GRID_SQARE
        new_y = head.ycor()
        head = snake[0]
        snake.pop(0)
        head.goto(new_x, new_y)
        if (abs(head.xcor()) >= GRID_SIZE * GRID_SQARE / 2) or (abs(head.ycor()) >= GRID_SIZE * GRID_SQARE / 2):
            is_continue = False
        for block in snake:
            print(block.pos())
        print(head.pos())
    return


GRID_SQARE = 20
GRID_SIZE = 30

screen = Screen()
screen.setup(width=GRID_SIZE * GRID_SQARE, height=GRID_SIZE * GRID_SQARE)
screen.bgcolor('black')
screen.title("Snake")
initial_setup()
screen.exitonclick()