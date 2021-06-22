from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(x=0, y=190)
        self.score_right = 0
        self.score_left = 0
        self.putscore()
        self.thewinner = ""

    def putscore(self):
        self.write("P1:{}     P2:{}".format(self.score_right, self.score_left), False, align="center",
                   font=("Comic Sans", 35, "normal"))

    def winner(self):
        if self.score_right == 5:
            self.thewinner = "Player 1"
        if self.score_left == 5:
            self.thewinner = "Player 2"
        self.goto(x=0, y=0)
        self.write("The winner is {}!".format(self.thewinner), False, align="center",
                   font=("Comic Sans", 50, "normal"))
