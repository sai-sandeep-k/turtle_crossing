from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-240, 250)
        self.update_level()

    def update_level(self):
        self.write(f" Level: {self.level}", align="center",font=("pixel", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", align="center", font=("pixel", 20, "normal"))

