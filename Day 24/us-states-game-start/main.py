import random
import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
state_count = 0


def display_state_name(state, x, y):
    t = turtle.Turtle()
    t.hideturtle()

    t.penup()
    t.goto(x, y)

    t.write(state, align="center", font=("Arial", 8, "normal"))


while game_is_on:

    data = pd.read_csv("50_states.csv")
    list_of_data = data.state.to_list()

    # random.choice(list_of_data)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name ?").title()
    if answer_state in data["state"].values:
        correct_state_row = data[data.state == answer_state]
        x_cor = correct_state_row.x.values[0]
        y_cor = correct_state_row.y.values[0]
        state_count += 1
        display_state_name(answer_state, x_cor, y_cor)
        if state_count == 150:
            game_is_on = False
        print(x_cor)
        print(y_cor)

        print(correct_state_row)

    # else:
    #     game_is_on = False

screen.exitonclick()
