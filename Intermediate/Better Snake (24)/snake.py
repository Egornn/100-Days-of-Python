from turtle import Turtle

DIRECTION_LIST = {'Up': 90, 'Left': 180, 'Right': 0, 'Down': 270}
GRID_SQUARE = 20
GRID_SIZE = 30
INITIAL_COORDINATES = [(-2, 0), (-1, 0), (0, 0)]
SHAPE = 'square'
COLOR = 'white'


class Snake:

    def __init__(self):
        self.segments = []
        self.is_continue = True
        self.dir = "Right"
        self.last_dir = "Right"
        self.create_snake()

    def extend(self):
        new_block = Turtle(shape=SHAPE, visible=False)
        new_block.penup()
        new_block.color(COLOR)
        new_block.goto(self.segments[0].pos())
        new_block.setheading(self.segments[0].heading())
        new_block.backward(GRID_SQUARE)
        new_block.showturtle()
        self.segments.insert(0, new_block)

    def create_snake(self):
        def add_turtle(x: int, y: int, snake_list=[]):
            new_turtle = Turtle(shape=SHAPE, visible=False)
            new_turtle.penup()
            new_turtle.color(COLOR)
            new_turtle.setposition(x * GRID_SQUARE, y * GRID_SQUARE)
            new_turtle.showturtle()
            snake_list.append(new_turtle)
            return snake_list

        for coordinates in INITIAL_COORDINATES:
            self.segments = add_turtle(coordinates[0], coordinates[1])

    def reset(self):
        self.is_continue = True
        self.dir = 'Right'
        self.last_dir = 'Right'
        for seg in self.segments:
            seg.goto(GRID_SQUARE * GRID_SIZE, GRID_SQUARE * GRID_SIZE)
        self.segments.clear()
        self.create_snake()

    def move_up(self):
        if self.last_dir != "Down":
            self.dir = 'Up'

    def move_down(self):
        if self.last_dir != "Up":
            self.dir = 'Down'

    def move_left(self):
        if self.last_dir != "Right":
            self.dir = 'Left'

    def move_right(self):
        if self.last_dir != "Left":
            self.dir = 'Right'

    def move(self):
        for i in range(len(self.segments) - 1):
            self.segments[i].forward(GRID_SQUARE)
        self.segments[-1].seth(DIRECTION_LIST[self.dir])
        self.segments[-1].forward(GRID_SQUARE)
        for i in range(len(self.segments) - 1):
            self.segments[i].seth(self.segments[i + 1].heading())
        if (abs(self.segments[-1].xcor()) >= GRID_SIZE * GRID_SQUARE / 2 - 1) or \
                (abs(self.segments[-1].ycor()) >= GRID_SIZE * GRID_SQUARE / 2 - 1):
            self.is_continue = False
        for x in self.segments[:-1]:
            if x.distance(self.segments[-1]) < GRID_SQUARE / 2:
                self.is_continue = False
        self.last_dir = self.dir
        return

    def is_overlap(self, food_tile: tuple) -> bool:
        for x in self.segments:
            if x.distance(food_tile) < GRID_SQUARE / 2:
                return True
        return False
