shoppingList = []


def addItem():
    shoppingList.append(input("What will be added?: "))


def removeItem():
    print("There are ", len(shoppingList), " items in the list.")
    try:
        shoppingList.pop(int(input("Which item is deleted?: ")))
    except IndexError:
        print("Incorrect selection.")


def main():
    running = True
    # print("The program has started!")
    while running:
        print()
        selector = int(input("Would you like to\n(1) Add or\n(2) Remove items"
                       " or\n(3) Quit?: "))
        if selector == 1:
            addItem()
        elif selector == 2:
            removeItem()
        elif selector == 3:
            running = False
            print("The following items remain in the list: ")
            for i in shoppingList:
                print(i)
        else:
            print("Incorrect selection.")


if __name__ == "__main__":
    main()
