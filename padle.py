from turtle import Turtle
class Paddles(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,1)
        self.setpos(pos)

    def go_up(self):
       n_ycor= self.ycor()+20
       self.setpos(self.xcor(),n_ycor)

    def go_down(self):
       n_ycor= self.ycor()-20
       self.setpos(self.xcor(),n_ycor)
 
    