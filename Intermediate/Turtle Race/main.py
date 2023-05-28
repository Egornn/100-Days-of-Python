from turtle import Turtle, Screen
from random import randint

def sketcher(turtle: Turtle, screen: Screen):
    def move_forward():
        turtle.forward(10)

    def move_backward():
        turtle.back(10)

    def turn_clockwise():
        turtle.right(10)

    def turn_counterclockwise():
        turtle.left(10)

    def clear():
        turtle.penup()
        turtle.clear()
        turtle.home()
        turtle.pendown()

    screen.listen()
    screen.onkeypress(key="w", fun=move_forward)
    screen.onkeypress(key="s", fun=move_backward)
    screen.onkeypress(key="d", fun=turn_clockwise)
    screen.onkeypress(key="a", fun=turn_counterclockwise)
    screen.onkey(key="c", fun=clear)


def race(turtle_number):
    def create_turtle(color, x, y):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x, y)
        return turtle

    def random_move():
        step_min = 10
        step_max = 20
        for turtle in turtle_racers:
            turtle.forward(randint(step_min, step_max))

    def step():
        random_move()

    def is_reached():
        for tu in turtle_racers:
            if tu.position()[0] >= - starting_line - spacing:
                return True

    def winner(racers) -> str:
        turtle_won = racers[0].color()
        winning_position = racers[0].position()[0]
        for turtle in racers:
            if turtle.position()[0] > winning_position:
                turtle_won = turtle.color()
                winning_position = turtle.position()[0]
        return turtle_won[0]

    screen.setup(500, 400)
    color_list = ['red', 'orange', 'yellow', 'green', 'blue',
                  'purple', 'pink', 'brown', 'gray', 'gold']
    turtle_racers = []
    spacing = 30
    screen.clear()
    is_finished = False
    if turtle_number > len(color_list):
        print(f'Maximum number of turtles is {len(color_list)}')
        return
    color = ""
    while not (color in color_list):
        color = screen.textinput("Make you bet", f'Choose a color from the list {color_list[:turtle_number]}')

    starting_line = - screen.window_width() / 2 + spacing
    for i in range (turtle_number):
        color = color_list[i]
        x = starting_line
        y = (turtle_number // 2 - i) * spacing - ((turtle_number+1) % 2) * spacing / 2
        turtle_racers.append(create_turtle(color, x, y))
    while not is_finished:
        step()
        is_finished = is_reached()
    result = winner(turtle_racers)
    if result == color:
        pop = "You've won!"
    else:
        pop = "You've lost"
    screen.textinput(f"{pop}", f"Winner is {result}")
    return


tim = Turtle()
screen = Screen()
sketcher(tim, screen)
race(10)
