import random
from pyfiglet import Figlet

#---Bracket Format---#
#print("Movie Name")
#print("-------------------------")
#print("                         |" + " Winning Movie")
#print("-------------------------")
#print("Movie Name")
#
# Bracket Function
def bracketRound(arrayTest, arrayCount):
    iterator = 0
    winnerArray = []
    while iterator < arrayCount - 1:
        match = Figlet(font='straight')
        print(match.renderText("Match #" + str(iterator+1)))
        winnerArray.append(arrayTest[iterator+1])
        print(arrayTest[iterator])
        print("-------------------------")
        print("                         | " + arrayTest[iterator+1])
        print("-------------------------")
        print(arrayTest[iterator+1])
        print("")
        arrayTest.pop(iterator)
        arrayCount = len(arrayTest)
        iterator = iterator + 1
    return(winnerArray)

#---Code---#
# TO-DO: Create Array/List Import (Add read .txt file, each newline is a new list item)
file = open("movies.txt", "r")
arrayPremade = file.readlines()
print(arrayPremade)
file.close()


# Using pre-created Array/List to start
#arrayPremade = ["Whoa", "Hey", "Odd", "Yo", "Anotha 1", "Wut", "Yee", "Skibidi"]
arrayPremadeCount = len(arrayPremade)

# Shuffle Array/List
arrayPremade = random.sample(arrayPremade, len(arrayPremade))

# Loop through Array/List, compare values, select winner, place winner in new Array/List, remove loser & winner from original list
roundCounter = 1
while arrayPremadeCount > 1:
    round = Figlet(font='stop')
    print(round.renderText("ROUND # " + str(roundCounter)))
    arrayPremade = bracketRound(arrayPremade, arrayPremadeCount)
    arrayPremadeCount = len(arrayPremade)
    arrayPremade = random.sample(arrayPremade, len(arrayPremade))
    roundCounter = roundCounter+1

# Print Winner
print("$------AND THE WINNER IS------$")
print("")
winner = Figlet(font='epic')
print(winner.renderText(arrayPremade[0]))
print("$-----------------------------$")


