from random import randint, choice
from turtle import Turtle
from player import GRID_SQUARE, GRID_SIZE
from scoreboard import STARTING_LEVEL

COLORS = ['red', 'yellow', 'purple', 'black', 'blue', "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENTAL = 10
TIME_STEP = 0.1


class CarManager:
    def __init__(self):
        self.active_cars = []
        self._generate_car()
        self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENTAL * (STARTING_LEVEL - 1)

    def car_generator_random(self, current_level):
        if (randint(0, 5 - current_level) == 0) or current_level > 3:
            self._generate_car()

    def _generate_car(self):
        car = Turtle(shape="square", visible=False)
        car.penup()
        car.color(choice(COLORS))
        car.shapesize(1, 2, 1)
        car.setposition(GRID_SQUARE * (GRID_SIZE / 2 + 1), randint(-GRID_SIZE / 2 + 3, GRID_SIZE / 2 - 3) * GRID_SQUARE)
        car.showturtle()
        self.active_cars.append(car)

    def move_car(self):
        for car in self.active_cars:
            car.goto(car.pos()[0] - self.speed, car.pos()[1])
        if self.active_cars[0].pos()[0] < -GRID_SQUARE * (GRID_SIZE + 4) / 2:
            self.active_cars.remove(self.active_cars[0])

    def is_collided(self, turtle: Turtle):
        for car in self.active_cars:
            if abs(car.pos()[1] - turtle.pos()[1]) < GRID_SQUARE:
                if turtle.distance(car) <= GRID_SQUARE:
                    return True
        return False

    def update_level(self):
        self.speed += MOVE_INCREMENTAL
