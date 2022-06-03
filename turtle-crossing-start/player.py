from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#Create player(turtle), starts at the bottom of the screen and can only move up with "Up" key
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def player_move(self):
        self.fd(20)

    def finish_line(self):
        self.goto(STARTING_POSITION)


