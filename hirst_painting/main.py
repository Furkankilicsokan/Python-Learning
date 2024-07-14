# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(218, 172, 126), (159, 180, 190), (132, 74, 55), (52, 102, 152), (117, 82, 93), (180, 143, 153),
              (160, 105, 150), (44, 48, 67), (128, 173, 115), (83, 95, 182), (66, 10, 29), (82, 133, 107),
              (227, 189, 144), (52, 63, 78), (192, 92, 74), (216, 225, 216), (114, 45, 59),
              (70, 66, 53), (94, 142, 118), (207, 183, 190), (179, 187, 213), (67, 59, 50), (208, 185, 178),
              (182, 201, 176), (78, 58, 53), (175, 198, 203), (58, 61, 60)]

paint = t.Turtle()
t.colormode(255)
paint.speed('fastest')
paint.hideturtle()

paint.penup()
y = -250
for _ in range(10):
    paint.teleport(-250, y)
    for _ in range(10):
        paint.forward(50)
        paint.dot(20, random.choice(color_list))
    y += 50

screen = t.Screen()
screen.exitonclick()
