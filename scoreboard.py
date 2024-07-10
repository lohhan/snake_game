from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

   def __init__(self):
      super().__init__()
      self.actual_score = 0
      self.hideturtle()
      self.penup()
      self.color("white")
      self.goto(0, 260)
      self.update_scoreboard()   
   
   def update_scoreboard(self):
      self.write(f"Scoreboard: {self.actual_score}", align=ALIGNMENT, font=FONT)
   
   def game_over(self):
      self.goto(0, 0)
      self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

   def increase_score(self):
      self.clear()
      self.actual_score += 1
      self.update_scoreboard() 