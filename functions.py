def main():
    running = True
    while running:
        text = input("Write something (quit ends): ")
        if text == "quit":
            running = False
            break
        booleani = subfunc(text)
        if booleani:
            print("X spotted!")


def subfunc(givenstring="Too short"):
    if len(givenstring) > 9 and "X" in givenstring:
        print(givenstring)
        return True
    elif len(givenstring) < 10:
        print("Too short")
        return False
    else:
        print(givenstring)


if __name__ == "__main__":
    main()
