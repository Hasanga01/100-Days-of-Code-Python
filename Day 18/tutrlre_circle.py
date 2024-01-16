from turtle import Turtle,Screen
import random

def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.pencolor((R, G, B))


tim = Turtle()
tim.speed("fastest")
tim.pensize(2)
for _ in range(36):
    tim.circle(200)
    heading = (tim.heading()+10)
    tim.setheading(heading)
    change_colour()


screeen =Screen()
screeen.exitonclick()