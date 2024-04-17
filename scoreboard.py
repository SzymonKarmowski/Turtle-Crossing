from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT, align="left")

    def level_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.write("GAME OVER", font=FONT, align="center")
