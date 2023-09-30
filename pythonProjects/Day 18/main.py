from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('red')


while True:
    timmy_the_turtle.color('red')
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)
    timmy_the_turtle.color('yellow')
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)
    timmy_the_turtle.color('sea green')
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)
    timmy_the_turtle.color('cyan')
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)


screen = Screen()
screen.exitonclick()
