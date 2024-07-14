from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_r) < 40 or ball.xcor() < -320 and ball.distance(paddle_l) < 40:
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 420:
        scoreboard.increase_score_l()
        ball.refresh()
        time.sleep(0.5)

    # Detect L paddle miss
    elif ball.xcor() < -420:
        scoreboard.increase_score_r()
        ball.refresh()
        time.sleep(0.5)

    if scoreboard.score_r == 5:
        game_is_on = False
        scoreboard.game_over_r()

    elif scoreboard.score_l == 5:
        game_is_on = False
        scoreboard.game_over_l()

screen.exitonclick()
