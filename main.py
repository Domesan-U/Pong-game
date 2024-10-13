import time

from paddle import Paddle
from turtle import Screen
from ball import Ball

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.tracer(0)
p1 = Paddle()
p2 = Paddle()
p1.paddle_position("left")
p2.paddle_position("right")
b = Ball()

s.update()
s.listen()

game_is_on = True
running = True


def pause():
    global running
    if (running):
        running = False
    else:
        running = True
    print(running)


while game_is_on:
    s.onkey(key="space", fun=pause)
    s.update()
    if running:
        time.sleep(0.09)
        b.move_ball()
        s.onkey(key="space", fun=pause)
        if b.b.xcor() > 390 or b.b.xcor() < -390:
              game_is_on = False
        if b.b.distance(p1.p) < 30 or b.b.distance(p2.p) < 30:
            print("paddle collide")
            b.paddle_collide()
        s.onkey(key="w", fun=p1.up)
        s.onkey(key="q", fun=p1.down)
        s.onkey(key="Up", fun=p2.up)
        s.onkey(key="Down", fun=p2.down)

s.onkey(key="space", fun=pause)

s.exitonclick()
