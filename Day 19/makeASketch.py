from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(100)


def move_backwards():
    tim.backward(100)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)

screen.exitonclick()
