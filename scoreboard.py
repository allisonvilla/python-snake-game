from turtle import Turtle

ALIGNMENT = "center"
FONT = ('gg Sans', 16, 'normal')
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self.display_score()

    def display_score(self):
        self.write(f"🐍 Score: {self.score} 🐍 High Score: {self.high_score} 🐍", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

