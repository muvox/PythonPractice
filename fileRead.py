import time
defaultFilename = "notebook.txt"
selectedBook = defaultFilename


def readnotes():
    file = open(selectedBook, "r")
    print(file.read())
    file.close()


def openDefault():
    try:
        open(defaultFilename, "r")
    except FileNotFoundError:
        print("No default notebook was found, created one.")
        open(defaultFilename, "w+").close()


def addnote():
    stamp = time.strftime("%X %x")
    file = open(selectedBook, "a")
    newNote = input("Write a new note: ") + ":::" + stamp + "\n"
    file.write(newNote)
    file.close()


def clearnotes():
    file = open(selectedBook, "w")
    file.write("")
    file.close()
    print("Notes deleted.")


def chooseFile():
    global selectedBook
    fileName = input("Give the name of the new file: ")
    try:
        open(fileName, "r")
    except FileNotFoundError:
        print("No notebook with that name detected, created one.")
        open(fileName, "w+")
        selectedBook = fileName
    else:
        selectedBook = fileName


def main():
    openDefault()
    running = True
    # print("The program has started!")
    while running:
        print("Now using file ", selectedBook)
        selector = int(input(
            "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n"
            "(4) Change the notebook\n(5) Quit\n\nPlease select one: "))
        if selector == 1:
            readnotes()
        elif selector == 2:
            addnote()
        elif selector == 3:
            clearnotes()
        elif selector == 4:
            chooseFile()
        elif selector == 5:
            print("Notebook shutting down, thank you.")
            running = False
        else:
            print("Incorrect selection.")


if __name__ == "__main__":
    main()
