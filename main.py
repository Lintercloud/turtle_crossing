import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_up, "Up")
screen.onkey(player.turtle_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    car_manager.make_cars()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_in_goal():
        player.turtle_reset()
        car_manager.level_up()
        scoreboard.increase_level()



