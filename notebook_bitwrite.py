import time
import pickle
defaultFilename = "notebook.dat"
selectedBook = defaultFilename
listOfNotes = []


def readnotes():
    for i in listOfNotes:
        print(i)


def saveFile():
    pickle.dump(listOfNotes, open(selectedBook, "wb"))


def openDefault():
    global listOfNotes
    try:
        file = open(defaultFilename, "rb")
        listOfNotes = pickle.load(file)
    except FileNotFoundError:
        print("No default notebook was found, created one.")
        file = open(defaultFilename, "wb+")
    except EOFError:
        # print("File was empty!")
        print("")


def addnote():
    stamp = time.strftime("%X %x")
    newNote = input("Write a new note: ") + ":::" + stamp + "\n"
    listOfNotes.append(newNote)
    saveFile()


def editNote():
    print("The list has ", len(listOfNotes), "notes.")
    selectedItem = int(input("Which of them will be changed?: "))
    print(listOfNotes[selectedItem])
    stamp = time.strftime("%X %x")
    newNote = input("Give the new note: ") + ":::" + stamp + "\n"
    listOfNotes[selectedItem] = newNote
    saveFile()


def deleteNote():
    print("The list has ", len(listOfNotes), "notes.")
    selectedItem = int(input("Which of them will be deleted?: "))
    try:
        print("Deleted note ", listOfNotes[selectedItem])
    except IndexError:
        print("Deleted note", listOfNotes[selectedItem - 1])
        listOfNotes.pop(selectedItem - 1)
    else:
        listOfNotes.pop(selectedItem)
    saveFile()


def main():
    openDefault()
    running = True
    # print("The program has started!")
    while running:
        # print("Now using file ", selectedBook)
        selector = int(input(
            "(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4)"
            " Delete a note\n(5) Save and quit\n\nPlease select one: "))
        if selector == 1:
            readnotes()
        elif selector == 2:
            addnote()
        elif selector == 3:
            editNote()
        elif selector == 4:
            deleteNote()
        elif selector == 5:
            print("Notebook shutting down, thank you.")
            running = False
        else:
            print("Incorrect selection.")


if __name__ == "__main__":
    main()
