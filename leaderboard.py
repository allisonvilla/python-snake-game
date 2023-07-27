from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Trebuchet MS', 14, 'normal')
COLOR = "white"
MAX_LINES = 10

# TODO: Sort scores from highest to lowest
# TODO: Show "Leaderboard" as a title
# TODO: Limit number of lines to 10


class Leaderboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.scores_list = []
        with open("leaderboard.txt") as data:
            unformatted_list = data.readlines()
            for entry in unformatted_list:
                self.scores_list.append(entry.strip().upper())

    def update_leaderboard(self, name, high_score):
        if high_score > 0:
            self.scores_list.extend([name, high_score])
            with open("leaderboard.txt", mode="a") as data:
                data.write(f"\n{name}\n{high_score}")

    def display_leaderboard(self):
        for num in range(int(len(self.scores_list) / 2)):
            position = 0, (255 - (num * 50))
            index = num * 2
            self.create_line(position, index)

    def create_line(self, position, index):
        new_line = Turtle()
        new_line.hideturtle()
        new_line.color(COLOR)
        new_line.hideturtle()
        new_line.penup()
        new_line.speed("fastest")
        new_line.goto(position)
        new_line.write(f"{self.scores_list[index]} . . . . . . . . . . . . . . . {self.scores_list[index + 1]}", move=False, align=ALIGNMENT, font=FONT)

