import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_color = (r,g,b)
  return random_color
degree = 0
t.speed('fastest')
for i in range(100):
  t.color(random_color())
  t.circle(100)
  degree += 1
  t.left(degree)
# def random_color():
#   r = random.randint(0,255)
#   g = random.randint(0,255)
#   b = random.randint(0,255)
#   random_color = (r,g,b)
#   return random_color
# degrees = [0, 90, 180, 270]
# for i in range(100):
#   # random_color = random.choice(colors)
#   tim.color(random_color())
#   tim.speed(10)
#   tim.pensize(15)
#   tim.right(random.choice(degrees))
#   tim.forward(30)
# def shape(corners):
#   for line in range(corners):
#     tim.right(360 / corners)
#     tim.forward(100)

# for i in range(3,11):
#   tim.pencolor(random.choice(colors))
#   shape(i)
screen = t.Screen()
screen.exitonclick()