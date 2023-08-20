from turtle import Turtle
from snake import GRID_SQUARE, GRID_SIZE

FONT = ('Sans', 22, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, GRID_SIZE * GRID_SQUARE / 2 - 2 * GRID_SQUARE)
        self.color('white')
        self.open_high_score()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.write_score()

    #
    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.write_score()

    def open_high_score(self):
        try:
            with open('highscore.txt', encoding="utf-8", mode='r') as f:
                # as a relative path to desktop '../../../Desktop/highscore.txt'
                self.high_score = int(f.read())
                f.close()
        except:
            with open('./highscore.txt', encoding="utf-8", mode='w') as f:
                f.write('0')
                f.close()

    def save_high_score(self):
        with open('./highscore.txt', encoding="utf-8", mode='w') as f:
            f.write(str(self.high_score))
            f.close()
