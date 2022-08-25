"""Module containing classes and methods for creating and operating paddles

Classes:
    Paddle
"""
MOVE = 20
from turtle import Turtle

class Paddle(Turtle):
    

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE)