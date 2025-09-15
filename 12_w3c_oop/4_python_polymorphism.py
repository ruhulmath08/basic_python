"""
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the
same name that can be executed on many objects or classes.
"""

# Example: with polymorphism
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Driving...")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sailing...")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flying...")


car = Car("Ford", "Mustang")
boat = Boat("Boeing", "747")
plane = Plane("Boeing", "777")
for x in (car, boat, plane):
    x.move()
"""


# Example: using polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Moving...")


class Car(Vehicle):

    def move(self):
        print("Driving...")


class Boat(Vehicle):
    def move(self):
        print("Sailing...")


class Plane(Vehicle):
    def move(self):
        print("Flying...")


car = Car("Ford", "Mustang")
boat = Boat("Boeing", "747")
plane = Plane("Boeing", "777")
for x in (car, boat, plane):
    x.move()
