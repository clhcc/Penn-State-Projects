# This program is to draw random numers side of polygons.

# Author: Linhan Cai

# Import modules.
import turtle
import random

# Print the header.
print('This program will draw a polygon with 3 or more sides. \n')

# Set the initial values and settings.
turtle.shape('turtle')
sides = int(input('Enter the number of sides, less than 3 to exit: '))
length = 600 / sides
width = (sides % 20) + 1

# Set the color list.
colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']

# The make_polygon function draws a polygon with the number of sides, side length, border color, border width, and fill color as specified.
def make_polygon (sides, length, border_color, width, fill_color):
    turtle.clear()
    angle = 360/sides
    turtle.pensize(width)
    turtle.pencolor(border_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()

# While loop.
while sides >= 3:
    rand1 = random.randint(0,12)
    border_color = colors[rand1]
    rand2 = random.randint(0, 12)
    fill_color = colors[rand2]
    make_polygon(sides, length, border_color, width, fill_color)
    sides = int(input('Enter the number of sides, less than 3 to exit: '))
else:
    print('Thanks for using the polygon generator program.')
