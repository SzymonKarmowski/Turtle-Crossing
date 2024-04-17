import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 24, "normal")
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
score = Scoreboard()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() == FINISH_LINE_Y:
        score.level_up()
        player.goto(STARTING_POSITION)
        car_manager.level_up()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

screen.exitonclick()
