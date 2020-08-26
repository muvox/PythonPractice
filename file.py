file = open("strings.txt", "r")
for line1 in file:
    line = line1.strip()
    if line.isalnum():
        print(line, "was ok.")
    else:
        print(line, "was invalid.")
