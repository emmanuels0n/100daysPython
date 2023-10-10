def add(*args):  # We can use the asterisk to add arguments
    print(args[3])  # I can access my added arguments by indexes, it is a tuple
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 5, 8))  # I can take as many values as I want


def calculate(n, **kwargs):  # double asterisk means I can pass unlimited kword arguments
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)  # I made a dictionary


class Car:

    def __init__(self, **kw):  # I can use kwargs in classes
        self.make = kw.get("make")
        self.model = kw.get("model")  # .get is used to prevent it from crashing in case no value is passed


my_car = Car(make="Nissan", model="GT_R")
