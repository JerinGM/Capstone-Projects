from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-395, 225)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.score}", False, "left", ("Arial", 15, "normal"))
        self.score +=1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!!", False, "center", ("Arial", 15, "normal"))
