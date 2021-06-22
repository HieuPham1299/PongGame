from turtle import Turtle


class Linesetup(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(2.5)
        self.penup()
        self.setposition(x=-595, y=240)
        self.pendown()
        self.forward(1180)
        self.setheading(-90)
        self.forward(475)
        self.setheading(-180)
        self.forward(1180)
        self.setheading(-270)
        self.forward(475)
        self.goto(x=0, y=240)
        self.setheading(-90)
        while self.ycor() > -240:
            self.forward(10)
            self.penup()
            self.forward(13)
            self.pendown()
