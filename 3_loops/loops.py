def while_loop(number):
    print("----------While loop----------")
    while number != 0:
        print("Number is", number)
        number = number - 1


def do_while_loop(number):
    print("----------Do while loop----------")
    while True:
        print("Number is", number)
        number = number - 1
        if number == 0:
            break


def for_loop(count):
    print("----------For loop----------")
    for i in range(count):
        print("Number is", i)


x = int(input("Enter a number: "))
while_loop(x)
do_while_loop(x)
for_loop(x)
