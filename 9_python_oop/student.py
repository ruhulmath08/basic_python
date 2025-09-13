class Student:
    # class constructor
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # string representation of the object
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house: str):
        if house not in ["dhaka", "rajshahi", "naogaon"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        return cls(
            name=input("Enter your name: "),
            house=input("Enter your house: "),
        )


def main():
    student_details = Student.get()
    print(student_details)


if __name__ == "__main__":
    main()
