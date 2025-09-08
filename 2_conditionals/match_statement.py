def main():
    name = str(input("Enter your name: ").lower())

    match name:
        case "ruhul":
            print("Engineer")
        case "rabby":
            print("Doctor")
        case "habib":
            print("Farmer")
        case _:
            print("Unknown")


main()
