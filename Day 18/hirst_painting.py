from turtle import Turtle, Screen
import random

import colorgram

tim = Turtle()


def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.pencolor((R, G, B))


# colors = colorgram.extract('spots.jpg', 10)

color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
              (238, 227, 5), (227, 159, 49)]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g,b)
#     color_list.append(new_colors)

# tim.goto(-350,-350)
tim.penup()
tim.hideturtle()
tim.setx(-350)
tim.sety(-350)
x = -350
y = -350

for position in range(8):

    for dots in range(8):
        tim.dot(40)
        tim.forward(100)
        change_colour()
    y += 100
    tim.setx(x)
    tim.sety(y)
# turtle.dot(200,"red")

screen = Screen()
screen.exitonclick()
# print(color_list)
