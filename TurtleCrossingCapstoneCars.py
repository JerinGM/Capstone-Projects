from turtle import Turtle
import random

colors = ["red", "yellow", "red", "green", "pink", "purple"]
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.emptylist = []
        self.hideturtle()
        self.carbackwardspeed = 10

    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            newobj = Turtle("square")
            newobj.hideturtle()
            newobj.penup()
            newobj.goto(380, random.randint(-220, 220))
            newobj.color(random.choice(colors))
            newobj.shapesize(1, 2)
            newobj.showturtle()
            self.emptylist.append(newobj)


    def move(self):
        for cars in self.emptylist:
            cars.backward(self.carbackwardspeed)

    def car_reset(self):
        self.carbackwardspeed += 5
        self.move()




