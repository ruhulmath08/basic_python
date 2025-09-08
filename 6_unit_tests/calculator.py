def main():
    x = int(input("Enter a number: "))
    print(f"The square of {x} is: {square(x)}")


def square(n):
    return n * n


# Ensures the code inside it runs only when the script is executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
