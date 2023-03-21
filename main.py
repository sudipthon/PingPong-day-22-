from turtle import Screen
from padle import Paddles
from ball import Ball
import time

from score import Score

screen = Screen()
ball = Ball()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
score=Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    ball.move()
    screen.update()     
    
# ball bouncing of upper and lower wall
    if ball.ycor() > 235 or ball.ycor()<-233:
        ball.bounce_wall()
        
#ball bouncing of r_paddle 
    if ball.xcor()>=320:
          if ball.distance(r_paddle) <= 60: 
            ball.bounce_paddle()
        
# ball bouncing of l_paddle
    if ball.xcor()<=-320: 
        if ball.distance(l_paddle) <= 60:
            ball.bounce_paddle()
           
# score counting and restarting game on miss   
    #when right padle misses
    if ball.xcor() >= 380 :
        ball.restart()
        score.score_l()
        
     #when right padle misses
    if ball.xcor() < -380 :
        ball.restart()
        score.score_r()
        # game_on=False

screen.exitonclick()
