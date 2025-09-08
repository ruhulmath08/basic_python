import statistics
import sys


def calculate_mean():
    print("Enter numbers separated by spaces:")
    user_input = sys.stdin.readline().strip()

    # print the user inpu values
    print(f"The input value is: [{user_input}]")

    # Convert input into a list of floats
    numbers = [float(x) for x in user_input.split()]

    # Return the mean value
    return statistics.mean(numbers)


def main():
    mean_value = calculate_mean()
    print(f"The mean value is: {mean_value}")


main()
