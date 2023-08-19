from turtle import Turtle

GRID_SIZE = 30
GRID_SQUARE = 20
STARTING_POSITION = (0, -(GRID_SIZE / 2 - 1) * GRID_SQUARE)
FINISH_LINE_Y = (GRID_SIZE / 2 - 1) * GRID_SQUARE
MOVE_DISTANCE = GRID_SQUARE / 2


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.is_next_level = False
        self.shape("turtle")
        self.penup()
        self.reset_next_level()

    def move_up(self):
        self.goto(self.pos()[0], self.pos()[1] + MOVE_DISTANCE)
        if self.pos()[1] >= FINISH_LINE_Y:
            self.is_next_level = True
        return

    def reset_next_level(self) -> None:
        self.hideturtle()
        self.setposition(STARTING_POSITION)
        self.seth(90)
        self.showturtle()
        self.is_next_level = False
