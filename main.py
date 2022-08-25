from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


WIDTH = 800
HEIGHT = 600
# Coordinates of Right (R) and Left (L) paddle
R_PADDLE = WIDTH//2-50
L_PADDLE = -WIDTH//2+50

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Arcade Game Pong")
screen.tracer(0)

# Initialize objects
paddle_right = Paddle((R_PADDLE, 0))
paddle_left = Paddle((L_PADDLE, 0))
ball = Ball()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Bounce from walls
    if ball.ycor() > HEIGHT//2 - 20 or ball.ycor() < - HEIGHT//2 + 20:
        ball.bounce_y()

    # Loosing condition
    if (ball.xcor() >= R_PADDLE and abs(ball.ycor() - paddle_right.ycor()) >= 50):
        scoreboard.l_point()
        ball.reset_position()

    if (ball.xcor() <= L_PADDLE and abs(ball.ycor() - paddle_left.ycor()) >= 50):
        scoreboard.r_point()
        ball.reset_position()

    # Bounce from paddles
    if ball.xcor() > R_PADDLE - 30:
        ball.if_bounce(paddle_right.xcor(), paddle_right.ycor())
        
    if ball.xcor() < L_PADDLE + 30:
        ball.if_bounce(paddle_left.xcor(), paddle_left.ycor())

    ball.move()

screen.exitonclick()