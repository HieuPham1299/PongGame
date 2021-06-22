from turtle import Screen
from paddle1 import Paddle1


class Paddle2(Paddle1):
    def __init__(self):
        super().__init__()
        self.goto(580, 0)

    def control(self):
        screen = Screen()
        screen.onkey(fun=self.up, key="Up")
        screen.onkey(fun=self.down, key="Down")
