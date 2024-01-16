import random
import turtle
from turtle import Turtle, Screen

screen = Screen()

colors = ["red", "green", "blue", "yellow", "pink", "brown"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

is_race_on = False
win_count = 0
screen.setup(width=500, height=400)
# user_input = screen.textinput("Make a bet", "Which turtle is going to finish first")
user_input = random.choice(colors)
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_input:
                print(f"You Won, The winning turtle  is :{winning_colour}")
                
            else:
                print(f"You lost, you chose {user_input} , The winning turtle  is :{winning_colour}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
