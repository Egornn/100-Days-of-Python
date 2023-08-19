from turtle import Screen
from time import sleep
from player import Player, GRID_SIZE, GRID_SQUARE
from car_manager import CarManager, TIME_STEP
from scoreboard import Scoreboard

game_over = False


def next_level():
    player.reset_next_level()
    scoreboard.update_level()
    cars.update_level()


screen = Screen()

screen.setup(width=GRID_SIZE * GRID_SQUARE, height=GRID_SIZE * GRID_SQUARE)
screen.bgcolor('white')
screen.title("Cross the Road")
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")
while not game_over:
    cars.move_car()
    cars.car_generator_random(scoreboard.level)
    if player.is_next_level:
        next_level()
    game_over = cars.is_collided(player)
    screen.update()
    sleep(TIME_STEP)
scoreboard.gameover()
screen.exitonclick()
