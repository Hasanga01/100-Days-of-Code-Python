from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xCor, yCor):
        super().__init__()
        self.x_cor = xCor
        self.y_cor = yCor
        self.shape("square")
        self.color("white")
        self.penup()

        self.goto(xCor, yCor)

        self.shapesize(5, 1)

    def up(self):
        new_y_cor = self.ycor() + 40
        self.goto(self.xcor(), new_y_cor)

    def down(self):
        new_y_cor = self.ycor() - 40
        self.goto(self.xcor(), new_y_cor)
