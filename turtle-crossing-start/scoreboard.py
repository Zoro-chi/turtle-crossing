from turtle import Turtle

import player
from player import Player

FONT = ("Courier", 24, "bold")
GAME_OVER = "GAME OVER"
LEVEL = 1

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-270, 270)
        self.write(f"Level : {self.level}", align="left", font=("courier", 20, "normal"))





    def game_over(self):
        self.goto(0, 0)
        self.write(f"{GAME_OVER}", align="center", font=FONT)

    def level_update(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align="left", font=("courier", 20, "normal"))




