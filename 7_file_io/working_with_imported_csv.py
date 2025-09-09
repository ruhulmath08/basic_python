import csv


def main():
    def read_file_from_csv_by_name_house():
        students = []
        with open("students_with_multi_comma.csv") as file:
            reader = csv.reader(file)
            for name, home in reader:
                students.append({"name": name, "home": home})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is in {student['home']}")

    # Read from csv by name and house using DictReader
    def read_file_from_csv_by_name_house_using_dict_reader():
        students = []
        with open("students_with_multi_comma.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "home": row["home"]})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is in {student['home']}")

    # Read from csv by name,home, and district
    def read_file_from_csv_by_name_house_district_using_dict_reader():
        students = []
        with open("students_with_name_address_district.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "home": row["home"], "district": row["district"]})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is in {student['home']} {student['district']}")

    read_file_from_csv_by_name_house_district_using_dict_reader()


if __name__ == "__main__":
    main()
