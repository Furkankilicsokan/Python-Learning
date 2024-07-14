from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_l} {self.score_r}", align="center", font=("Courier", 50, "bold"))

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def game_over_l(self):
        self.goto(0, 0)
        self.write("GAME OVER LEFT WON", align="center", font=("Courier", 35, "bold"))

    def game_over_r(self):
        self.goto(0, 0)
        self.write("GAME OVER RİGHT WON", align="center", font=("Courier", 35, "bold"))
