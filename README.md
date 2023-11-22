# Bracket-Challenge
## Concept
The Bracket Challenge will take an input list of items, assign them random values, then assign them to a bracket structure. Once the structure is set, the bracket will weight the randomly assigned values against each other to determine a winner. At each round, a new list of the remaining winners is created and randomly assigned values again to ensure higher randomness. The rounds continue until there is a final winner.

## Bracket Format
```
Movie Name #1
-------------------------
                         | Winning Movie
-------------------------
Movie Name #2
```

## To-Do
1. Create Array/List Import (Add read .txt file, each newline is a new list item)
2. Create handling for Corner Case
3. Add more randomness on the individual bracket winner

## Corner Cases
1. Problem: Odd Array/List count
   Solution 1: Take one item out of list, assign random value, compare to final movie
   Solution 2: Reject Array/List for not being even

## Dependencies
- python3
- pyfiglet
- random (maybe default package)