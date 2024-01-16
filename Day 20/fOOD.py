from turtle import Turtle
import random


# Blue apple that snake eats to get bigger
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ramdom_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(ramdom_x, random_y)
