# Importing files
from turtle import Turtle


# Creating the field line class to draw the middle line
class FieldLine(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.25, stretch_len=1)
        self.penup()
        self.goto(0, 300)
        self.draw_line()

    # This method to draw the line
    def draw_line(self):
        for _ in range(20):
            self.setheading(270)
            self.stamp()
            self.forward(50)

