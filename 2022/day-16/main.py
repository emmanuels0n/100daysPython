# # import turtle #Importing the turtle module
# #
# # timmy = turtle.Turtle() # Importing the "Turtle" class from turtle module, or...
#
# from turtle import Turtle, Screen  #Turtle is an external library
#
# timmy = Turtle()  # This is an object created from a blueprint
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOliveGreen4")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)  # Before the dot it is the object, after the dot it is the attribute (the method)
# # object.method()
# my_screen.exitonclick()  # Function (method)

# To look for python packages go into PyPi (Pithon Package Index), to install a package go into file>settings>
# >project>python interpreter>"+">install the package (PrettyTable)
# import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Sqirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

table.align = "l"
print(table)
