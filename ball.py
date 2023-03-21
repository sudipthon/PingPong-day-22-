from turtle import Turtle, circle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x=15
        self.y=15
     
    def move(self):
        self.goto(self.xcor()+self.x,self.ycor()+self.y)
    def bounce_wall(self):
       self.y *= -1
    
    def bounce_paddle(self):
       self.x *= -1
       
    def restart(self):
        self.bounce_paddle()
        self.goto(0,0)
        self.move()
        

                 
