from turtle import Turtle

ALIGNMENT = "center"
FONT = ('gg Sans', 16, 'normal')
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
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
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_closed(self):
        self.goto(0, 0)
