from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initializating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initializating the objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Setting the keyboards commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Starting the game
game_is_on = True
while game_is_on:
   screen.update()      
   time.sleep(0.1)
   
   snake.move()

   # Detect collision with food
   if snake.head.distance(food) < 15:
      food.refresh_coordinates()
      snake.extend()
      scoreboard.increase_score()

   # Detect collision with wall
   if snake.head.xcor() == 300 or snake.head.xcor() == -300 or snake.head.ycor() == 300 or snake.head.ycor() == -300:
      scoreboard.game_over()
      game_is_on = False

   # Detect collision with the tail
   for segment in snake.snake_body[1:]:
      if snake.head.distance(segment) < 10:
         scoreboard.game_over()
         game_is_on = False
      
# Setting to the screen not exit when I run the code 
screen.exitonclick()