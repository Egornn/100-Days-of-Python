from turtle import Turtle, Screen
from random import randint


def draw_ngon(corner, size):
    for i in range(corner):
        timmy.forward(size)
        timmy.right(360 / corner)


def generate_color():
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def draw_line(dash_length, repeats):
    for i in range(repeats):
        timmy.forward(dash_length)
        timmy.penup()
        timmy.forward(dash_length)
        timmy.pendown()


def draw_set_of_ngons(turtle, up_to_n, size):
    for i in range(3, up_to_n + 1):
        turtle.pencolor(generate_color())
        draw_ngon(i, size)


def random_walk(turtle, steps):
    orientation = [0, 90, 180, 270]
    turtle.pensize(10)
    for i in range (steps):
        turtle.pencolor(generate_color())
        turtle.setheading(orientation[randint(0, len(orientation)-1)])
        turtle.forward(20)


def draw_spirograph(turtle, rotations, size):
    for i in range(rotations):
        turtle.pencolor(generate_color())
        turtle.circle(size)
        turtle.left(360 / rotations)


def initial_setup():
    screen.colormode(255)
    timmy.speed("fastest")


def paint(turtle: Turtle, screen_visible: Screen):
    step, size = 50, 25
    screen.clear()
    initial_setup()
    turtle.setposition(-screen_visible.window_width() / 2 + step, -screen_visible.window_height() / 2 + step)
    turtle.setheading(0)
    turtle.penup()
    while turtle.pos()[1] < screen_visible.window_height() / 2 - step:
        while turtle.pos()[0] < screen_visible.window_width() / 2 - step:
            turtle.dot(size, generate_color())
            turtle.forward(step)
        new_line = (-screen_visible.window_width() / 2 + step, turtle.pos()[1] + step)
        turtle.setposition(new_line)
    turtle.setposition(0, 0)


screen = Screen()
timmy = Turtle()
screen.colormode(255)
timmy.color('red')
initial_setup()

# Draw a square
timmy.goto(100,0)
timmy.right(90)
draw_ngon(4, 125)

# Draw a doted line
timmy.right(90)
draw_line(10, 15)

# Draw up to deca
draw_set_of_ngons(timmy, 10, 125)

# Draw random walk
screen.clear()
timmy.goto(0,0)
initial_setup()
random_walk(timmy, 100)

# Draw spirograph
timmy.pensize(1)
draw_spirograph(timmy, 50, 100)

# Paint a picture
paint(timmy, screen)
screen.exitonclick()
