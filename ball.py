from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 6
        self.y_move = 6

    def horizontal_collision(self):
        self.y_move *= -1

    def verticle_collision(self):
        self.x_move *= -1

    def moving(self):
        if self.x_move < 0:
            self.x_move -= 0.005
        else:
            self.x_move += 0.005

        if self.y_move < 0:
            self.y_move -= 0.005
        else:
            self.y_move += 0.005

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
