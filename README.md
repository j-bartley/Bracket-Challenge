# Bracket-Challenge
## Concept
The Bracket Challenge will take an input list of items, assign them random values, then assign them to a bracket structure. Once the structure is set, the bracket will weight the randomly assigned values against each other to determine a winner. At each round, a new list of the remaining winners is created and randomly assigned values again to ensure higher randomness. The rounds continue until there is a final winner.

## Bracket Format
Movie Name #1
/-------------------------
/                         | Winning Movie
/-------------------------
Movie Name #2

## To-Do
1. Create Array/List Import (Preferably Excel)
2. Create Array/List to hold names & values
3. Randomly assign values to each name (Array/List item)
4. Split Array/List into bracket format
5. Compare values, determine winners
6. Gather winners, go to step 2, exit after only 1 winner remaining

## Corner Cases
1. Problem: Odd Array/List count
   Solution 1: Take one item out of list, assign random value, compare to final movie
   Solution 2: Reject Array/List for not being even