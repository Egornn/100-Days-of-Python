from turtle import Screen, Turtle
from random import randint

DIRECTION_LIST = {'Up': 90, 'Left': 180, 'Right': 0, 'Down': 270}
GRID_SQUARE = 20
GRID_SIZE = 30
INITIAL_COORDINATES = [(-2, 0), (-1, 0), (0, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.is_continue = True
        self.dir = "Right"
        self.create_snake()

    def create_snake(self):
        def add_turtle(x: int, y: int, snake_list=[]):
            new_turtle = Turtle(shape='square', visible=False)
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.setposition(x * GRID_SQUARE, y * GRID_SQUARE)
            new_turtle.showturtle()
            snake_list.append(new_turtle)
            return snake_list

        for coordinates in INITIAL_COORDINATES:
            self.segments = add_turtle(coordinates[0], coordinates[1])

    def move_up(self):
        if self.dir != "Down":
            self.dir = 'Up'

    def move_down(self):
        if self.dir != "Up":
            self.dir = 'Down'

    def move_left(self):
        if self.dir != "Right":
            self.dir = 'Left'

    def move_right(self):
        if self.dir != "Left":
            self.dir = 'Right'

    def move(self):
        for i in range(len(self.segments)-1):
            self.segments[i].forward(GRID_SQUARE)
        self.segments[-1].seth(DIRECTION_LIST[self.dir])
        self.segments[-1].forward(GRID_SQUARE)
        for i in range(len(self.segments) - 1):
            self.segments[i].seth(self.segments[i + 1].heading())
        if (abs(self.segments[-1].xcor()) >= GRID_SIZE * GRID_SQUARE / 2) or \
                (abs(self.segments[-1].ycor()) >= GRID_SIZE * GRID_SQUARE / 2):
            self.is_continue = False

        return

