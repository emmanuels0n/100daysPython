from turtle import Turtle  # We are making the food class inherit the properties from the Turtle class
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # All of these methods come from the Turtle Superclass
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
