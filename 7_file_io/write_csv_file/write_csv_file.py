import csv


def main():
    def write_csv_file():
        name = input("What's your name? ")
        home = input("What's your home? ")

        with open("csv_file.vsv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([name, home])

    def read_csv_file_using_dict_writer():
        name = input("What's your name? ")
        home = input("What's your home? ")

        with open("csv_file.vsv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"])
            writer.writerow({"name": name, "home": home})

    # write_csv_file()
    read_csv_file_using_dict_writer()


main()
