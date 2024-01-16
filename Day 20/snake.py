import turtle
from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        screen_positions = [(0, 0), (-20, 0), (-40, 0)]

        for positions in screen_positions:
            self.add_segment(positions)

    def add_segment(self, positions):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(positions)
        self.segments.append(new_turtle)

    def move_snake(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.segments[0].forward(20)

        # segments[0].left(90)
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # all snake movements through keyboard inputs
    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        # if self.head.heading() != UP:
        self.head.setheading(270)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
