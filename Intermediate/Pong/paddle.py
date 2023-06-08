from turtle import Turtle

STEP = 20
LIMIT_Y = 240
LIMIT_X = 370

class Paddle(Turtle):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.penup()
        self.x_pos = x
        self.y_pos = y
        self.setposition(self.x_pos, self.y_pos)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.showturtle()

    def move_up(self):
        if self.pos()[1] < LIMIT_Y:
            self.goto(self.x_pos, self.y_pos + STEP)
            self.x_pos, self.y_pos = self.pos()
        else:
            return

    def move_down(self):
        if self.pos()[1] > -LIMIT_Y:
            self.goto(self.x_pos, self.y_pos - STEP)
            self.x_pos, self.y_pos = self.pos()
    