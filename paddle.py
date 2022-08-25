"""Module containing classes and methods for creating and operating paddles

Classes:
    Paddle(Turtle)
        creates a paddle as a turtle object

Methods:
    go_up() 
        moves paddle up
    go_down()
        moves paddle down

Constants:
    MOVE
        controls how fast does the paddle move
"""

from turtle import Turtle

MOVE = 20

class Paddle(Turtle):
    """Create a paddle that one uses to bounce ball back on the other side

    Args:
        Turtle (class): superclass of class Paddle
    """
    
    def __init__(self, position):
        """Creates paddle object that bounces the ball
        """
        
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move paddle up
        """

        self.goto(self.xcor(), self.ycor() + MOVE)

    def go_down(self):
        """Move paddle down
        """

        self.goto(self.xcor(), self.ycor() - MOVE)