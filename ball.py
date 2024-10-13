from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.b = None
        self.new_y = 10
        self.new_x = 10
        self.create_ball()

    def create_ball(self):
        self.b = Turtle("circle")
        self.b.color("white")
        self.b.penup()
        self.b.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move_ball(self):
        self.b.speed("slow")
        if self.b.ycor() >= 260 or self.b.ycor() <= -260:
            self.new_y = self.new_y * -1
        print(self.new_y)
        self.b.goto(self.b.xcor() + self.new_x, self.b.ycor() + self.new_y)

    def paddle_collide(self):
        self.new_x = self.new_x * -1
