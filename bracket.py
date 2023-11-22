import random

#---Bracket Format---#
#print("Movie Name")
#print("-------------------------")
#print("                         |" + " Winning Movie")
#print("-------------------------")
#print("Movie Name")

#---To-Do---#
# 1. Create Array/List Import (Preferably Excel)
# 2. Create Array/List to hold names & values
# 3. Randomly assign values to each name (Array/List item)
# 4. Split Array/List into bracket format
# 5. Compare values, determine winners
# 6. Gather winners, go to step 2, exit after only 1 winner remaining

#---Code---#
# 1. Create Array/List Import (Preferably Excel)
# 2. Create Array/List to hold names & values 
# Using pre-created Array/List to start
arrayTest = ["Whoa", "Hey", "Odd", "Yo", "Anotha 1", "Wut", "Yee", "Skibidi"]
arrayCount = len(arrayTest)
iterator = 0
# Shuffle Array/List
random.shuffle(arrayTest)
random.shuffle(arrayTest)
random.shuffle(arrayTest)
# 3. Randomly assign values to each name (Array/List item)
# Loop through Array/List, compare values, select winner, place winner in new Array/List, remove loser & winner from original list
winnerArray = []

while iterator < arrayCount - 1:
    winnerArray.append(arrayTest[iterator+1])
    arrayTest.pop(iterator)
    arrayCount = len(arrayTest)
    iterator = iterator + 1

print(winnerArray)
# 11/21/23 - Left Off At Notes:
# - The initial first round of brackets appears to be working great
# - Need to implement this as a class/method so that it can be called independently of the amount of items