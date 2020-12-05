import random


def compare(c1, c2):
    if c1 == c2:
        print(c1+"   "+c2)
        print("equal")
        return 0
    elif (c1 == "R") & (c2 == "P"):
        print("R    P")
        print("You Lost")
        return -1
    elif (c1 == "R") & (c2 == "S"):
        print("R    S")
        print("You Won")
        return 1
    elif (c1 == "P") & (c2 == "R"):
        print("P    R")
        print("You Won")
        return 1
    elif (c1 == "P") & (c2 == "S"):
        print("P    S")
        print("You Lost")
        return -1
    elif (c1 == "S") & (c2 == "R"):
        print("S    R")
        print("You Lost")
        return -1
    elif (c1 == "S") & (c2 == "P"):
        print("S    P")
        print("You Won")
        return 1


List = ["R", "P", "S"]
myScore = 0
playerScore = 0


while (myScore < 3) & (playerScore < 3):

    playerChoice = str(input("play: "))
    myChoice = random.choice(List)
    score = compare(playerChoice, myChoice)
    if score > 0:
        playerScore += 1
    elif score < 0:
        myScore += 1

if playerScore == 3:
    print("Congrats! You Won")
elif myScore == 3:
    print("Sorry! You Lost")
