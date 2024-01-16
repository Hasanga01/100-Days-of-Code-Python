import time
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from Scoreboard import ScoreBoard

screen = Screen()
tim = Turtle()
screen.tracer(0)
ball = Ball()
score = ScoreBoard()

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)

game_is_on = True

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_l.up, "w")

screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 412:

        ball.goto(0, 0)
        ball.x_move = -10
        ball.move_speed = 0.05
        score.l_point()

    elif ball.xcor() < -412:
        ball.goto(0, 0)
        ball.x_move = 10
        ball.move_speed = 0.05
        score.r_point()
        # game_is_on = False
        # ball.write(align="center", arg="Game over", font=('Courier', 24, 'normal'))

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if paddle_r.distance(ball) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if paddle_l.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()
