import re


def main():
    # Using Regular Expressions
    """
    . -> Any character except newline
    * -> 0 or more repetitions
    + -> 1 or more repetitions
    ? -> 0 or 1 repetition
    {m} -> m repetitions
    {m, n} -> m to n repetitions
    ^ -> Start of string
    $ -> End of string (before newline) or end of string
    [abc] -> a or b or c
    [^abc] -> Not a, b, or c
    """

    def validate_email(pa: re.Pattern, email: str):

        if re.search(pa, email):
            print(f"{email} is a valid email")
        else:
            print(f"{email} is not a valid email")


    user_email = input("Enter your email: ")

    validate_email(re.compile(r".+@.+\.com"), user_email)

    validate_email(re.compile(r"^.+@.+\.com$"), user_email)

main()
