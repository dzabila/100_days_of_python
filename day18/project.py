import random
import colorgram
import turtle as t

# colors = colorgram.extract("day18/image.jpg", 30)
# colors_rgb = []
# for i in colors:
#   r = i.rgb.r
#   g = i.rgb.g
#   b = i.rgb.b
#   new_color = (r,g,b)
#   colors_rgb.append(new_color)

# print(colors_rgb)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
t.colormode(255)
def random_color():
  random_c = random.choice(color_list)
  r = random_c[0]
  g = random_c[1]
  b = random_c[2]
  new_color = (r,g,b)
  return new_color
t.penup()
t.setposition(-150, -150)
t.speed('fastest')
position_y = -150
for x in range(10):
  for y in range(10):
    t.dot(20, random_color())
    t.forward(50)
  position_y += 50
  t.setposition(-150, position_y)
t.setposition(-150,-150)
screen = t.Screen()
screen.exitonclick()