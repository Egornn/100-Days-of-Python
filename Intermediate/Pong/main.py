from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def white_line():
    line = Turtle()
    line.hideturtle()
    line.setposition(0, 300)
    line.color('white')
    line.pensize(5)
    while line.pos()[1] > -300:
        line.goto(line.pos()[0], line.pos()[1] - 20)
        line.penup()
        line.goto(line.pos()[0], line.pos()[1] - 15)
        line.pendown()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
white_line()
is_game = True
player_1 = Paddle(-350, 0)
player_2 = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

while is_game:
    screen.update()
    ball.move_ball(scoreboard)
    ball.bounce_of_paddle(player_1)
    ball.bounce_of_paddle(player_2)
    screen.onkey(player_2.move_up, 'Up')
    screen.onkey(player_2.move_down, 'Down')
    screen.onkey(player_1.move_up, 'w')
    screen.onkey(player_1.move_down, 's')
