# Need to start: 7:00: https://www.youtube.com/watch?v=nLRL_NcnK-4

def main():
    def write_name_in_file():
        file = open("names.txt", "a")
        name = input("Enter your name: ")
        file.write(f"{name}\n")
        file.close()

    def write_name_in_file_better_approach():
        name = input("Enter your name: ")
        with open("names.txt", "a") as file:
            file.write(f"{name}\n")

    # Read file
    def read_files():
        with open("names.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print("Hello,", line)

    # Read file better approach
    def read_files_better_approach():
        with open("names.txt", "r") as file:
            for line in file:
                # rstrip() remove the trailing whitespace
                print("Hello,", line.rstrip())

    # Read file and short approach
    def read_files_and_short():
        names = []
        with open("names.txt") as file:
            for line in file:
                names.append(line.rstrip())
        for name in sorted(names):
            print(f"Hello, {name}")  # Read file and short approach

    # Read file and short simplified approach
    def read_files_and_short_simplified_approach():
        with open("names.txt") as file:
            for line in sorted(file, reverse=True):
                print(f"Hello, {line.rstrip()}")

    # write_name_in_file()
    # write_name_in_file_better_approach()
    # read_files()
    # read_files_better_approach()
    # read_files_and_short()
    read_files_and_short_simplified_approach()


main()
