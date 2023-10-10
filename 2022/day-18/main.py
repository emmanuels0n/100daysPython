# from turtle import Turtle, Screen  # import the Turtle class
#
# tim = Turtle()  # An object from that class
# tim.shape("turtle")
# tim.color("red") # is possible to use colors in rgb from a tk color specification
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

import turtle as t

tim = t.Turtle()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range (3, 11):
    draw_shape(shape_side_n)





# screen = Screen()  # This must happen at the end of all the stuff with turtle
# screen.exitonclick()
