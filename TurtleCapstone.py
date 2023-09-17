from turtle import Turtle


class TurtleCross (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.goto(0, -230)
        self.left(90)
        self.showturtle()

    def up(self):
        self.forward(10)

    def reset(self):
        #self.hideturtle()
        self.goto(0, -230)
        #self.showturtle()