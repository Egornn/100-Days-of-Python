from car_manager import GRID_SQUARE, GRID_SIZE
from turtle import Turtle

STARTING_LEVEL = 1
FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = STARTING_LEVEL
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-GRID_SQUARE * GRID_SIZE / 3, -GRID_SQUARE * GRID_SIZE / 2)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.goto(-GRID_SQUARE * GRID_SIZE / 3, -GRID_SQUARE * GRID_SIZE / 2)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
