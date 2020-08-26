running = True


def namepassword():
    username = "John"
    password = "ABC123"

    inputname = input("Give name: ")
    if inputname == username:
        inputpw = input("Give password: ")
        if inputpw == password:
            print("Both inputs are correct!")
        else:
            print("The password is incorrect.")
    else:
        print("The given name is wrong.")


def numberSelector():
    numberoni = int(input("Select a number (1-3): "))
    if numberoni == 1:
        print("You selected one.")
    elif numberoni == 2:
        print("You selected two.")
    elif numberoni == 3:
        print("You selected three.")
    else:
        print("From one to three (1-3) dumb dumb")


def numbersEven():
    number1 = int(input("Give a number: "))
    number2 = int(input("Give another number: "))
    if (number1 % 2) == 0 and (number2 % 2) == 0:
        print("Both numbers are even.")
    elif (number1 % 2) == 0 or (number2 % 2) == 0:
        print("One number is even.")
    else:
        print("Both numbers are odd.")


def calculator():
    print("Calculator")
    running = True
    number1 = int(input("Give the first number: "))
    number2 = int(input("Give the second number: "))
    while running:

        def printStuff(numberoni):
            print("The result is: ", numberoni)

        selector = int(input(
            "(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Quit\nCurrent"
            "numbers: {} {}\nPlease select something (1-6): \n"
            .format(number1, number2)))
        if selector == 1:
            result = number1 + number2
            printStuff(result)
        elif selector == 2:
            result = number1 - number2
            printStuff(result)
        elif selector == 3:
            result = number1 * number2
            printStuff(result)
        elif selector == 4:
            result = number1 / number2
            printStuff(result)
        elif selector == 5:
            number1 = int(input("Give the first number: "))
            number2 = int(input("Give the second number: "))
        elif selector == 6:
            print("Thank you!")
            running = False
        else:
            print("Selection was not correct.")


def forNumberLoop():
    number = int(input("Give a number: "))
    number2 = 0
    for n in range(0, number):
        number2 = number2 + n
    print("The sum was: ", number2)


while running:
    selector = int(input(
        "Choose program to go for: \n 1: namepassword \n 2: numberselector"
        "\n 3: numberseven \n 4: calculator\n5: fornumbersloop\n"))
    if selector == 1:
        namepassword()
    elif selector == 2:
        numberSelector()
    elif selector == 3:
        numbersEven()
    elif selector == 0:
        running = False
    elif selector == 4:
        calculator()
    elif selector == 5:
        forNumberLoop()
