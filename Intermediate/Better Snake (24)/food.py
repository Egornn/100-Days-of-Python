from turtle import Turtle
from random import randint
from snake import GRID_SQUARE, GRID_SIZE


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.refresh()
        self.shapesize(stretch_wid=GRID_SQUARE/20, stretch_len=GRID_SQUARE/20)
        self.color('blue')
        self.speed('fastest')

    def refresh(self):
        self.goto(GRID_SQUARE * randint(-int((GRID_SIZE - 2) / 2), int((GRID_SIZE - 2) / 2)),
                  GRID_SQUARE * randint(-int((GRID_SIZE - 2) / 2), int((GRID_SIZE - 2) / 2)))
