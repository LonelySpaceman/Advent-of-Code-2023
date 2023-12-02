## DAY 2 PART 2 ##
import re

#load and open file
input = open('input.txt','r')
fileLines = [line.strip() for line in input.readlines()]

#get list of games
gameList = [line.split(':')[1] for line in fileLines]

#iterate through games
cubeColors = ['red','green','blue']
powerSum = 0
for game in gameList:
    
    gamePower = 1
    for color in cubeColors:
        matchString = f"(\d+) {color}"
        gamePower = gamePower * max([int(num) for num in re.findall(matchString, game)])

    powerSum += gamePower

print(f"Sum of power of all sets: {powerSum}")