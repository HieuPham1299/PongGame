from turtle import Screen
import time
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from scoreboard import Scoreboard
from linesetup import Linesetup

screen = Screen()
screen.setup(width=1200, height=500)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

line = Linesetup()
paddle1 = Paddle1()
paddle2 = Paddle2()
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

paddle1.control()
paddle2.control()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.005)
    ball.moving()

    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.horizontal_collision()

    if (ball.distance(paddle1) <= 90 or ball.distance(paddle2) <= 90) and (ball.xcor() > 565 or ball.xcor() < -570):
        ball.verticle_collision()

    if ball.xcor() > 600 or ball.xcor() < -600:
        scoreboard.clear()
        if ball.xcor() > 600:
            scoreboard.score_right += 1
            scoreboard.putscore()
        if ball.xcor() < -600:
            scoreboard.score_left += 1
            scoreboard.putscore()
        ball.y_move = 6
        ball.x_move = 6
        ball.goto(0, 0)
        time.sleep(0.5)

    if scoreboard.score_left == 5 or scoreboard.score_right == 5:
        scoreboard.winner()
        time.sleep(1)
        break


screen.exitonclick()
