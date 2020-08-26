try:
    filename = input("Give the filename: ")
    file = open(filename, "r")
except FileNotFoundError:
    print("There seems to be no file with that name.")
except IOError:
    print("There was a problem with the program.")
else:
    try:
        filedata = file.read().replace('\n', '')
        numbers = int(filedata)
    except ValueError:
        print("The file contents were unsuitable.")
    except IOError:
        print("There was a problem with the program.")
    else:
        print("The result was", (1000 / numbers))
