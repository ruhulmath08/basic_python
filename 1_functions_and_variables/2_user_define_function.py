def say_hello(to):
    print(f"Hello {to}")


def say_hell0_with_default_value(to="myself"):
    print(f"Hello {to}")

def say_bye(to):
    return f"Bye bye {to}"


name = input("Enter your name: ")
say_hello(name)
say_hell0_with_default_value()
byMessage = say_bye(name)
print(byMessage)

