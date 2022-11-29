# Importing files
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from fieldLine import FieldLine
import time

# Making the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Creating the paddles and ball objects
pong_net = FieldLine()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball()
scores = Scoreboard()

# Creating keyboard events to move the user paddle
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Looping until the game is finished
game_is_on = True
while game_is_on:
    time.sleep(pong_ball.ball_speed)
    screen.update()
    pong_ball.ball_move()

    # Detect collision with the wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.ball_bounce()

    # Detect collision with the paddle
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 \
            or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.ball_deflect()

    # Detect if the ball passes the paddles
    if pong_ball.xcor() > 400:
        pong_ball.ball_reset()
        scores.l_point()

    if pong_ball.xcor() < -400:
        pong_ball.ball_reset()
        scores.r_point()

screen.exitonclick()
