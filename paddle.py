from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.p = None
        self.create_paddle()

    def create_paddle(self):
        self.p = Turtle("square")
        self.p.color("white")
        self.p.shapesize(stretch_len=1, stretch_wid=4)
        self.p.penup()

    def paddle_position(self, pos):
        if pos == "left":
            self.p.goto(-380, 0)
        elif(pos == "right"):
            self.p.goto(380, 0)
        else:
            print("Enter proper position")

    def up (self):
        new_y = self.p.ycor()+20
        if(new_y<=260):
            self.p.goto(self.p.xcor(), new_y)

    def down (self):
        new_y = self.p.ycor()-20
        if(new_y>=-260):
            self.p.goto(self.p.xcor(), new_y)