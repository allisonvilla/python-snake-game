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
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"🐍 Score: {self.score} 🐍", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("😢 GAME OVER 😢", move=False, align=ALIGNMENT, font=FONT)
