import time
from turtle import Screen
from snake import Snake
from fOOD import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    scoreBoard.gen_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.score += 1
        scoreBoard.gen_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        
        scoreBoard.reset()
        snake.reset_snake()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreBoard.reset()
            snake.reset_snake()

screen.exitonclick()
