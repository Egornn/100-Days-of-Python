from turtle import Turtle
from snake import GRID_SQUARE, GRID_SIZE


FONT = ('Sans', 28, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, GRID_SIZE*GRID_SQUARE/2 - 2*GRID_SQUARE)
        self.color('white')
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
