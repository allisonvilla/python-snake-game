from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Trebuchet MS', 14, 'normal')
TITLE_FONT = ('Trebuchet MS', 18, 'normal')
COLOR = "white"
MAX_SCORES = 10


class Leaderboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 255)
        self.scores_list = []
        with open("leaderboard.txt") as data:
            # Get names and high scores from file and create dictionaries to append to scores_list
            unformatted_list = data.readlines()
            for index in range(0, len(unformatted_list) - 1):
                new_dict = {"name": "", "score": 0}
                if index % 2 == 0:
                    new_dict["name"] = unformatted_list[index].strip().upper()
                    new_dict["score"] = int(unformatted_list[index + 1].strip())
                    self.scores_list.append(new_dict)
        self.sort_leaderboard()

    def sort_leaderboard(self):
        # Sort scores_list from highest to lowest scores
        self.scores_list = sorted(self.scores_list, key=lambda x: x['score'], reverse=True)
        # Only show top 10 high scores
        if len(self.scores_list) > MAX_SCORES:
            self.scores_list = self.scores_list[0:MAX_SCORES]

    def update_leaderboard(self, name, high_score):
        if high_score > 0:
            self.scores_list.append({"name": name.strip().upper(), "score": high_score})
            with open("leaderboard.txt", mode="a") as data:
                data.write(f"\n{name}\n{high_score}")
            self.sort_leaderboard()

    def display_leaderboard(self):
        self.write("🐍 LEADERBOARD 🐍", move=False, align=ALIGNMENT, font=TITLE_FONT)
        for num in range(len(self.scores_list)):
            position = 0, (200 - (num * 50))
            self.create_line(position, num)

    def create_line(self, position, index):
        new_line = Turtle()
        new_line.hideturtle()
        new_line.color(COLOR)
        new_line.hideturtle()
        new_line.penup()
        new_line.speed("fastest")
        new_line.goto(position)
        new_line.write(f"{self.scores_list[index]['name']} . . . . . . . . . . . . . . . {self.scores_list[index]['score']}", move=False, align=ALIGNMENT, font=FONT)
