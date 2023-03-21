import turtle as tm
from random import choice
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("img.jpeg", 12)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(224, 164, 68), (130, 71, 119), (227, 120, 204), (84, 185, 180), (139, 124, 167), (71, 157, 144), (112, 141, 49), (252, 246, 251), (109, 138, 47)]
t = tm.Turtle()
tm.colormode(255)

color = choice(color_list)
t.setheading(225)
t.penup()
t.forward(250)
t.setheading(0)
start_x = t.position()[0]
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    color = choice(color_list)
    t.dot(20, color)
    t.forward(50)
    if i % 10 == 0:
        t.setpos(start_x, t.position()[1] + 50)

sc = tm.Screen()
sc.exitonclick()
