## DAY 2 PART 1 ##
import re

#load and open file
input = open('input.txt','r')
fileLines = [line.strip() for line in input.readlines()]

#set color limits
colorLimits = {'red':12,'green':13,'blue':14}

#get list of games
gameList = [line.split(':')[1].split(';') for line in fileLines]

#iterate through games
impossibleIndexSum = 0
for index, game in enumerate(gameList):
    possibleGame = True

    for subset in game:
        #get all cube picks for subset
        cubePicks = re.findall(r"(\d+) ([a-z]+)", subset)
        for pick in cubePicks:
            number = int(pick[0])
            color = pick[1]

            if number > colorLimits[color]: 
                possibleGame = False
    
    if possibleGame: impossibleIndexSum += index + 1

print(f"Sum of impossible game IDs: {impossibleIndexSum}")