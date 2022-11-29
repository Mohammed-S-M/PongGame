# Importing files
from turtle import Turtle


# Create the Ball blueprint class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_shape()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    # Ball shape
    def ball_shape(self):
        self.color("yellow")
        self.shape("circle")
        self.penup()

    # This method to make the ball move
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # This method to make the ball bounce when hit the wall
    def ball_bounce(self):
        self.y_move *= -1

    # This method to make the ball deflect when hit the paddle
    def ball_deflect(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    # This method to reset the ball back to the center after a player won a round
    def ball_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_move *= -1
