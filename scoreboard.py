from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

   def __init__(self):
      super().__init__()
      self.actual_score = 0
      with open("data.txt") as file:
         self.high_score = int(file.read())
      self.hideturtle()
      self.penup()
      self.color("white")
      self.goto(0, 260)
      self.update_scoreboard()   
   
   def update_scoreboard(self):
      self.clear()
      self.write(f"Score: {self.actual_score} | Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
   
   def reset(self):
      if self.actual_score > self.high_score:
         self.high_score = self.actual_score
         with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
      self.actual_score = 0
      self.update_scoreboard()

   def increase_score(self):
      self.actual_score += 1
      self.update_scoreboard() 