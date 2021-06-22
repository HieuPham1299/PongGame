from turtle import Turtle, Screen


class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.goto(-590, 0)

    def up(self):
        if self.ycor() <= 190:
            self.forward(80)
        else:
            pass

    def down(self):
        if self.ycor() >= -190:
            self.backward(80)
        else:
            pass

    def control(self):
        screen = Screen()
        screen.onkey(fun=self.up, key="w")
        screen.onkey(fun=self.down, key="s")
