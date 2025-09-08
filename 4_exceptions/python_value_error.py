"""
SyntaxError
Exception
"""


def main():
    def python_value_error():
        try:
            x = int(input("Enter an int value: "))
            print("The integer value is:", x)  # This line only runs if int conversion succeeds
        except ValueError:
            print("Please enter a valid integer number")

    def python_value_error_with_else():
        try:
            x = int(input("Enter an int value: "))
        except ValueError:
            print("Please enter a valid integer number")
        else:
            print("The integer value is:", x)

    def user_input_until_valid():
        while True:
            try:
                x = int(input("Enter an int value: "))
                print("The integer value is:", x)
            except ValueError:
                print("Please enter a valid integer number")
            else:
                break

    def more_simplify_version():
        while True:
            try:
                return int(input("Enter an int value: "))
            except ValueError:
                print("Please enter a valid integer number")

    # python_value_error()
    # python_value_error_with_else()
    # user_input_until_valid()
    print(more_simplify_version())


main()
