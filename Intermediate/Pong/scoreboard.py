from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.goto(-100, 200)
        self.write(self.score_1, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.score_2, align='center', font=('Courier', 80, 'normal'))

    def update_score(self, ball):
        self.clear()
        if ball.pos()[1] > 0:
            self.score_1 += 1
        else:
            self.score_2 += 1
        self.setposition(-100, 200)
        self.write(self.score_1, align='center', font=('Courier', 80, 'normal'))
        self.setposition(100, 200)
        self.write(self.score_2, align='center', font=('Courier', 80, 'normal'))

