from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph():
    for _ in range(int(360 / 5)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 5)


draw_spirograph()
screen = Screen()
screen.exitonclick()