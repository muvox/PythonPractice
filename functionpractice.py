import random

wins = 0
ties = 0
rounds = 0


def computerChooses(playerString):
    player = int(playerString)
    computerSelection = random.randint(1, 3)
    if computerSelection == 2:
        print("Computer chose: Nuke")
    elif computerSelection == 1:
        print("Computer chose: Foot")
    else:
        print("Computer chose: Cockroach")

    comp = computerSelection
    if comp == 2 and player == 2:
        print("Both LOSE")
        roundCounter(0)
    elif comp == player:
        print("It is a tie!")
        roundCounter(2)
    elif (comp == 1 and player == 2) or \
         (comp == 2 and player == 3) or \
         (comp == 3 and player == 1):
        print("You WIN!")
        roundCounter(1)
    else:
        print("You LOSE!")
        roundCounter(0)


def roundCounter(outcome=0):
    global rounds
    global wins
    global ties
    if outcome == 1:
        wins = wins+1
        rounds = rounds + 1
    elif outcome == 2:
        ties = ties+1
        rounds = rounds + 1
    else:
        rounds = rounds + 1


def main():
    running = True
    while running:
        playerSelection = input("Foot, Nuke or cockroach? (Quit ends):")
        if playerSelection == "Foot":
            print("You chose: Foot")
            computerChooses(1)
        elif playerSelection == "Nuke":
            print("You chose: Nuke")
            computerChooses(2)
        elif playerSelection == "Cockroach":
            print("You chose: Cockroach")
            computerChooses(3)
        elif playerSelection == "Quit":
            print("You played {} rounds, and won {} rounds, playing tie in"
                  " {} rounds." .format(rounds, wins, ties))
            running = False
        else:
            print("Incorrect selection.")


if __name__ == "__main__":
    # execute only if run as a script
    main()
