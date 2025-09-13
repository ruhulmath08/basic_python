import random


class Hat:
    houses = ["dhaka", "rajshahi", "naogaon", ]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
