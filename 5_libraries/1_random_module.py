import random  # This means importing everything from the random module
from random import choice  # This means importing only the choice function from the random module
from random import randint


def main():
    def coin_flip_using_import_everything():
        print("------------------Coin flip using import everything------------------")
        coin = random.choice(["Heads", "Tails"])
        return coin

    def coin_flip_using_import_specific():
        print("------------------Coin flip using import specific------------------")
        coin = choice(["Heads", "Tails"])
        return coin

    def python_randint_function():
        print("------------------Python randint function------------------")
        number = randint(1, 6)  # This means generating a random number between 1 and 6
        return number

    def python_shuffle_function():
        print("------------------Python shuffle function------------------")
        cards = ["Ace", "King", "Queen", "Jack"]
        print("Actual value ", cards)
        random.shuffle(cards)
        return cards

    # Coin flip using import everything
    print("Coin flip by import everything: ", coin_flip_using_import_everything())
    print("Coin flip by import specific: ", coin_flip_using_import_specific())

    # Python randint function
    print("Python randint function: ", python_randint_function())

    # Python shuffle function
    print("Python shuffle function: ", python_shuffle_function())


main()
