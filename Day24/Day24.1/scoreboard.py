from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.save_score_to_file()
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def read_score_from_file(self):
        with open("data.txt") as data:
            return int(data.read())

    def save_score_to_file(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")