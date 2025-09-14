def main():
    # THIS IS A TEST
    yell_using_map("This", "is", "a", "test")

    # THIS IS A TEST
    yell_using_list("This", "is", "a", "test")


def yell_using_map(*words):
    uppercase = map(str.upper, words)
    print(*uppercase)


def yell_using_list(*words):
    uppercase = [word.upper() for word in words]
    print(*uppercase)


if __name__ == "__main__":
    main()
