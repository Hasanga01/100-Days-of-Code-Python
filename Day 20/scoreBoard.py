from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_Score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def gen_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score :{self.high_score_read()}", align="center", font=('Courier', 24, 'normal'))

    def reset(self):
        if self.score > self.high_Score:
            self.high_Score = self.score
            self.high_score_write()

        self.score = 0
        self.gen_score()

    # def game_over(self):
    #     self.hideturtle()
    #     self.penup()
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=('Courier', 24, 'normal'))

    def high_score_write(self):
        with open("high score.txt", mode='w') as file:
            file.write(f"{self.high_Score}")

    def high_score_read(self):
        with open("high score.txt", mode='r') as file2:
            content = file2.read()
        return content
