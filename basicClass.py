class Player:
    # Player-class: stores data on team colors and points.

    teamcolor = ""
    points = 0

    def __init__(self):
        self.teamcolor = input("What color do I get?: ")

    def getColor(self):
        return self.teamcolor

    def getPoints(self):
        return self.points

    def setPoints(self, givenPoints):
        self.points = givenPoints

    def setColor(self, givenColor):
        self.teamcolor = givenColor

    # def getInfo(self):
        # print("The ", self.teamcolor, " contender has ", self.points,\
        # "points\
        # ")

    def tellScore(self):
        print("I am", self.teamcolor, ", we have {} points!"
              .format(self.points))

    def goal(self):
        self.points = self.points + 1


def main():
    player1 = Player()
    player2 = Player()
    player1.goal()
    player1.goal()
    player2.goal()
    player1.tellScore()
    player2.tellScore()


if __name__ == "__main__":
    main()
