## DAY 5 PART 1 ##
import re

INPUT_FILE = 'input.txt'
#load and open file
input = open(INPUT_FILE,'r')
fileLines =  input.readlines()

#get seed list
seeds = re.findall(r"(\d+)", fileLines[0])

#get list of maps
maps = []
for line in fileLines[2:]:
    if re.match(r"\w+\-to\-\w+ map\:", line): lineMap = []
    elif line == "\n": maps.append(lineMap)
    else: lineMap.append(re.findall(r"(\d+)",line))
maps.append(lineMap)

#iterate through all seeds
locationNums = []
for seed in seeds:
    currentNumber = int(seed)

    #iterate through all maps
    for map in maps:

        #iterate through all transformations to see
        #if the current number is contained within any transformation
        for transform in map:
            destRangeStart = int(transform[0])
            sourceRangeStart = int(transform[1])
            rangeLength = int(transform[2])

            if currentNumber <= sourceRangeStart + rangeLength - 1 and currentNumber >= sourceRangeStart:
                mapOffset = currentNumber - sourceRangeStart
                currentNumber = destRangeStart + mapOffset
                break

    locationNums.append(currentNumber)

print(f"Lowest Location Number: {min(locationNums)}")