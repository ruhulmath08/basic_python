def main():
    # Read csv file
    def read_csv_file():
        with open("students.csv") as file:
            for line in file:
                name, location = line.rstrip().split(",")
                print(f"{name} is from {location}")

    # Read csv file and short
    def read_csv_file_and_short():
        students = []
        with open("students.csv") as file:
            for line in file:
                name, location = line.rstrip().split(",")
                students.append(f"{name} is from {location}")

        for student in sorted(students):
            print(student)

    def get_name(student):
        return student["name"]

    # Read csv file and short and better approach

    def read_csv_file_and_short_and_better_approach():
        students = []
        with open("students.csv") as file:
            for line in file:
                name, location = line.rstrip().split(",")
                student = {"name": name, "house": location}
                students.append(student)

        # for student in sorted(students, key=get_name, reverse=True):
        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is from {student['house']}")

    # read_csv_file()
    # read_csv_file_and_short()
    read_csv_file_and_short_and_better_approach()


main()
