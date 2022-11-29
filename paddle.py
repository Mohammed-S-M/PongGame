# Importing files
from turtle import Turtle


# Creating Paddle blueprint class inherit from Turtle class
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle_shape_position(position)

    # Paddle shape and position
    def paddle_shape_position(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # To make the paddle move up
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # To make the paddle move down
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
