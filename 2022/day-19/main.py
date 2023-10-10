from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    tim.right(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()  # makes the screen object start listening
screen.onkey(move_forward, "w")  # The previously defined function but without the parenthesis
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
