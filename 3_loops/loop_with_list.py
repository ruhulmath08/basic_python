def for_loop_with_list():
    print("----------For loop with list----------")
    number_list = [4, 5, 6]
    for number in number_list:
        print(f"{number_list.index(number)} element is: {number}")


def for_loop_with_range():
    print("----------For loop with range----------")
    for i in range(5):
        print("Number is", i)


def for_loop_without_unused_variable():
    print("----------For loop without unused variable----------")
    for _ in range(3):
        print("Loop without unused variable")


def loop_with_user_input():
    print("----------Loop with user input----------")
    while True:
        user_input = int(input("What's n?: "))
        if user_input < 0:
            print("Please enter a positive number")
            continue
        else:
            break
    for _ in range(user_input):
        print("Hello")


def loop_with_str_list():
    print("----------Loop with string list----------")
    name_list = ["Ruhul", "Rabby", "Habib"]
    for name in name_list:
        print(name)


def loop_with_str_list_details():
    print("----------Loop with string list details----------")
    name_list = ["Ruhul", "Rabby", "Habib"]
    for name in range(len(name_list)):
        print(name, name_list[name])


def loop_with_dictionary():
    names = {
        "Ruhul": "Naogaon",
        "Rabby": "Dhaka",
        "Reza": "Chapai",
        "Jahangir": "Rajshahi"
    }

    for name in names:
        print(f"User: {name}, from :{names[name]}")


def print_students_with_index():
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]
    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")


# for_loop_with_list()
# for_loop_with_range()
# for_loop_without_unused_variable()
# loop_with_user_input()
# loop_with_str_list()
# loop_with_str_list_details()
# loop_with_dictionary()
print_students_with_index()
