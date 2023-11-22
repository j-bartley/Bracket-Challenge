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
# Using pre-created Array/List to start
arrayTest = ["test", "test2", "test3"]
arrayCount = len(arrayTest)
iterator = 0

print(arrayTest)
random.shuffle(arrayTest)
random.shuffle(arrayTest)
random.shuffle(arrayTest)

while iterator <= arrayCount - 1:
    print(arrayTest[iterator])
    iterator = iterator + 1
