from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(10)
def move_backward():
  tim.backward(10)
def turn_left():
  tim.left(30)
def turn_right():
  tim.right(30)
def reset():
  tim.home()
  tim.clear()
  
screen.listen()
screen.onkey(key="w", fun=move_forward)#როდესაც ერთ ფუნქციას მეორეს გადავცემთ ფრჩხილი არ უნდა
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()