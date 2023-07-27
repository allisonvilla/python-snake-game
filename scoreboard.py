from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Trebuchet MS', 14, 'normal')
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.current_high_score = 0
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}  |  HIGH SCORE: {self.current_high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset_game(self):
        if self.score > self.current_high_score:
            self.current_high_score = self.score
        self.score = 0
        self.display_score()

    def game_closed(self):
        self.goto(1000, 1000)

    def get_high_score(self):
        return self.current_high_score
