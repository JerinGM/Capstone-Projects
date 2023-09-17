from turtle import Turtle, Screen
from TurtleCapstone import TurtleCross
from TurtleCrossingCapstoneCars import Car
from scoreTurtlecrossCapstone import Score


import random
import time


screen = Screen()
screen.tracer(0)
screen.setup(800, 500)
screen.bgcolor("white")

turtle = TurtleCross()

car = Car()
score = Score()

screen.listen()
screen.onkey(fun=turtle.up, key="Up")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move()
    for item in car.emptylist:
        if item.distance(turtle) < 30:
            score.game_over()
            gameOn = False

    if turtle.ycor() == 240:
        turtle.reset()
        score.update()
        car.car_reset()





screen.exitonclick()