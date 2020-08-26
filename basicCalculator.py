import math


def printStuff(numberoni):
    print("The result is: ", numberoni)


def numberer():
    falseInput = True
    while falseInput:
        try:
            num = int(input("Give a number: "))
        except ValueError:
            print("This input is invalid.")
        else:
            falseInput = False
    return num


print("Calculator")
number1 = numberer()
number2 = numberer()
running = True
while running:
    selector = int(input("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)"
                         "\n(6)cos(number1/number2)\n(7)Change numbers\n(8)"
                         "Quit\nCurrent numbers:{} {}\nPlease select something"
                         "(1-6): \n".format(number1, number2)))
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
        result = math.sin(number1 / number2)
        printStuff(result)
    elif selector == 6:
        result = math.cos(number1 / number2)
        printStuff(result)
    elif selector == 7:
        number1 = numberer()
        number2 = numberer()
    elif selector == 8:
        print("Thank you!")
        running = False
    else:
        print("Selection was not correct.")
