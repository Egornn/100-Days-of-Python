import time
from turtle import Turtle
from paddle import STEP, LIMIT_Y, LIMIT_X
from random import randint
from paddle import Paddle

SLEEP = 0.1
SPEED_MULT = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.direction_x = randint(0, 1) * 2 - 1
        self.direction_y = randint(0, 1) * 2 - 1
        self.step = STEP
        self.current_speed = SLEEP

    def move_ball(self, scoreboard):
        if self.pos()[1] >= (LIMIT_Y + 2 * STEP) or self.pos()[1] <= - (LIMIT_Y + 2 * STEP):
            self.direction_y *= -1
        if self.pos()[0] > LIMIT_X or self.pos()[0] < - LIMIT_X:
            self.reset_pos()
            scoreboard.update_score(self)
        new_x = self.pos()[0] + self.direction_x * self.step / 2
        new_y = self.pos()[1] + self.direction_y * self.step / 2
        self.goto(new_x, new_y)
        time.sleep(self.current_speed)

    def reset_pos(self):
        self.direction_x = randint(0, 1) * 2 - 1
        self.direction_y = randint(0, 1) * 2 - 1
        self.setposition(0, 0)
        self.current_speed = SLEEP

    def bounce(self):
        self.direction_x *= -1

    def bounce_of_paddle(self, paddle: Paddle):
        if ((330 <= self.pos()[0] < 350 and self.direction_x == 1) or
            (-350 < self.pos()[0] <= -330 and self.direction_x == -1)) and \
                self.distance(paddle) <= 50:
            self.direction_x *= -1
            self.current_speed *= SPEED_MULT
