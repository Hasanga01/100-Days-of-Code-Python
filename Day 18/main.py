import random
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
# tim.color("green")
tim.pensize(5)
sides = 90

occurrence = random.randint(0, 100)
directions = [0,90,180,270]

def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.pencolor((R, G, B))


#tim.speed(50)


# for _ in range(500):
#
#     choice = random.randint(0,2)
#     tim.forward(100)
#     tim.setheading(random.choice(directions))
#     # change_colour()
#     # sides += 1

screen = Screen()
screen.exitonclick()
