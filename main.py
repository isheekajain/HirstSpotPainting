import random
import turtle as turtle
# import colorgram

# rgb_colors = []

# Extract 80 colors from an image.
# colors = colorgram.extract('image.jpg', 80)

# for i in colors:
#   r = i.rgb.r
#   g = i.rgb.g
#   b = i.rgb.b
#   final_colors = (r, g, b)
#   rgb_colors.append(final_colors)

# print(rgb_colors)
my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()


full_list = [(187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176), (87, 22, 58), (182, 188, 209), (118, 122, 149), (94, 16, 15)]

x = -250
y = -250


def paint_row():
    my_turtle.goto(x, y)
    for _ in range(10):
        my_turtle.dot(20, random.choice(full_list))
        my_turtle.penup()
        my_turtle.forward(50)


for _ in range(10):
    paint_row()
    y += 50

screen = turtle.Screen()
screen.exitonclick()
