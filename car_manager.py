from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE =  10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def make_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(300, 350), random.randint(-250, 250))
            self.cars.append(new_car)

    def level_up(self):
        self.speed += MOVE_INCREMENT