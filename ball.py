"""Module controling behavior of the ball

Classes:
    Ball(Turtle)
        Creates ball as a Turtle object

Methods:
    move()
        moves ball
    bounce_y()
        bounces ball from the upper and lower wall
    bounce_x()
        bounces ball from the paddle and increase the speed of the ball
    if_bounce()
        checks if the ball is in range of the paddle
    reset_position()
        reset ball's position and start moving in direction of the player
        who scored a point

Constants:
    MOVE_SPEED
        controls initial speed of the ball
"""

from turtle import Turtle, speed

MOVE_SPEED = 0.1

class Ball(Turtle):
    """Create the ball object and model its behavior

    Args:
        Turtle (class): superclass of Ball class
    
    Atributes:
        x_move:
            change of ball's position in x-direction in each iteration
        y_move:
            change of ball's position in y-direction in each iteration
        move_speed:
            speed of the ball
    """

    def __init__(self):
        """Creates the ball object
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        """Move the ball.
        """

        self.goto((self.xcor() + self.x_move, self.ycor() + self.y_move))

    def bounce_y(self):
        """Bounce the ball in the y-direction.
        """

        self.y_move *= -1

    def bounce_x(self):
        """Bounce in the x-direction and increase speed of the ball.
        """
        self.x_move *= -1
        self.move_speed *= 0.9
        

    def if_bounce(self, paddle_x, paddle_y):
        """Check if the ball should bounce.

        Args:
            paddle_x (int): x coordinate of the center of the paddle
            paddle_y (int): y coordinate of the center of the paddle
        """
        if  abs(paddle_x - self.xcor()) <= 20 and abs(self.ycor() - paddle_y) <= 50:
            self.bounce_x()
        

    def reset_position(self):
        """After scoring a point, reset ball to its initial position and initial speed.
        """

        self.goto(0,0)
        self.bounce_x()
        self.move_speed = MOVE_SPEED

   
    
