class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    """
    pass -> used when you want to create an empty class
    """
    #pass

    def __init__(self, fname, lname, passing_year):
        super().__init__(fname, lname)
        self.passing_year = passing_year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.passing_year)

student = Student("Mohammed", "Ali", 2015)
student.printname() # Mohammed Ali
print(student.passing_year) #2015
student.welcome() # Welcome Mohammed Ali to the class of 2015