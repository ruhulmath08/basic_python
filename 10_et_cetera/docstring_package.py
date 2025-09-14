# docstrings -> how to document your code

def meow(n: int) -> str:
    """
    Meow n times.
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an integer
    :return A string of n meows, one per line.
    :rtype str
    """
    return "meow\n" * n


number: int = int(input("Enter a number: "))
meows: str = meow(number)
print(meows, end="")

#  pip install mypy -> install mypy: type checking
#  mypy meows.py -> check type in the file
