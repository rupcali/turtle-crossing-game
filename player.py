from turtle import Turtle
from scoreboard import Scoreboard
scoreboard = Scoreboard()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move(self):
        current_y = self.ycor()
        current_x = self.xcor()
        current_y += MOVE_DISTANCE
        self.goto(current_x, current_y)
        
    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False
