def main():
    x = int(input("Enter a number: "))

    if is_even_value(x):
        print(f"The number {x} is even")
    else:
        print(f"The number {x} is odd")


def is_even(x):
    return True if x % 2 == 0 else False

# more pythonic way
def is_even_value(x):
    return x % 2 == 0


main()
