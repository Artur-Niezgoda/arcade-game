from turtle import Turtle, speed

MOVE_SPEED = 0.1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        self.goto((self.xcor() + self.x_move, self.ycor() + self.y_move))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        

    def if_bounce(self, paddle_x, paddle_y):
        if  abs(paddle_x - self.xcor()) <= 20 and abs(self.ycor() - paddle_y) <= 50:
            self.bounce_x()
        

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = MOVE_SPEED

   
    