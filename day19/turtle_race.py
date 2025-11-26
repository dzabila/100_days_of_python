from turtle import Turtle, Screen
import random

is_race_on = False
#setting up screen
screen = Screen()
screen.setup(width=500, height=400)
#setting up turtles
turtle_one = Turtle()
turtle_two = Turtle()
turtle_three = Turtle()
#giving shape to turtles
turtle_one.shape("turtle")
turtle_two.shape("turtle")
turtle_three.shape("turtle")
#giving colors to turtles
turtle_one.color("red")
turtle_two.color("green")
turtle_three.color("blue")
#making every pen up on turtles
turtle_one.penup()
turtle_two.penup()
turtle_three.penup()
#giving starting positions to turtles
turtle_one.goto(x=-240, y=-100)
turtle_two.goto(x=-240, y=0)
turtle_three.goto(x=-240, y=100)


user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle will win? Enter Color: ")


screen.exitonclick()
