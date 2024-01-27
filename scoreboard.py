from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

#TODO: 5. Create a scoreboard
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
