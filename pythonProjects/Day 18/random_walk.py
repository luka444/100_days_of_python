from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
tim.pensize(15)
for _ in range(50):
    tim.color(random.choice(colours))
    tim.forward(40)
    tim.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()