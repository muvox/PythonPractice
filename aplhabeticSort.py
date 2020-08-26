file = open("words.txt", "r")
listOfStuff = file.read().splitlines()
file.close()
listOfStuff.sort()
print("Words in an alphabetical order: ")
for i in listOfStuff:
    print(i)
