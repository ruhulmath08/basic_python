class Person:
    # constructor -> call every time object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # string representation of object
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def print_name(self):
        print("Hello my name is: ", self.name)


p1 = Person("John", 36)
print(p1)
p1.print_name()
del p1 # delete object