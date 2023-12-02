## DAY 1 PART 2 ##
import re

#load and open file
input = open('input.txt','r')

fileLines = [line.strip() for line in input.readlines()]

WORDMAP = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}
#list of strings to watch for in the line
strings2watch = [key for key in WORDMAP.keys()] + [WORDMAP[key] for key in WORDMAP.keys()]

calValues = []
for line in fileLines:

    matches = re.findall(r"(?=(" + '|'.join(strings2watch) + r"))", line)

    #get string of integers in each line
    calString = ''
    for match in matches:
        try:
            calString += WORDMAP[match]
        except KeyError: 
            calString += match
    
    #get list of integers made of of first and last integer in calString
    calValues.append(int(calString[0] + calString[-1]))

print(f"Sum of calibration values: {sum(calValues)}")