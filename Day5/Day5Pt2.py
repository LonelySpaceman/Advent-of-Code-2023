## DAY 5 PART 2 ##
import re
import os
import time

INPUT_FILE = 'input.txt'
#load and open file
input = open(INPUT_FILE,'r')
fileLines =  input.readlines()

#get seed list
seedRanges = [range(int(seed[0]),int(seed[0]) + int(seed[1])) for seed in re.findall(r"(\d+) (\d+)", fileLines[0])]

#get list of maps
mapsList = []
for line in fileLines[2:]:
    if re.match(r"\w+\-to\-\w+ map\:", line): lineMap = []
    elif line == "\n": mapsList.append(lineMap)
    else: lineMap.append(re.findall(r"(\d+)",line))
mapsList.append(lineMap)

#translate maps into a list of range objects
class RangeMap:
    def __init__(self, mapList:list, childRangeMap=None) -> None:
        self.childRangeMap = childRangeMap
        self.mapList = []
        for map in mapList:
            destinationRangeStart = int(map[0])
            sourceRangeStart = int(map[1])
            rangeLength = int(map[2])

            self.mapList.append({
                'sourceRange' : range(sourceRangeStart, sourceRangeStart + rangeLength),
                'destinationRange' : range(destinationRangeStart, destinationRangeStart + rangeLength),
                'rangeTransform' : sourceRangeStart - destinationRangeStart #add this number to transform from destination to source
            })
    
    def dest2source(self, destinationNum: int):
        #DESTINATION NUMBER MAY BE CONTAINED IN MULTIPLE DESTINATION RANGES
        self.mapStack = [map for map in self.mapList if destinationNum in map['destinationRange']]

        #add null transform to mapStack if the destination number is not contained within any map
        if len(self.mapStack) == 0:
            self.mapStack.append({'sourceRange' : None, 'destinationRange' : None, 'rangeTransform' : 0})

        childRangeMap = self.childRangeMap
        for map in self.mapStack:
            sourceNumber = destinationNum + map['rangeTransform']

            if childRangeMap is None: return sourceNumber
            else: return childRangeMap.dest2source(sourceNumber)

mapCascade = RangeMap(mapsList[0])
for mapList in mapsList[1:]:
    mapCascade = RangeMap(mapList, mapCascade)

#test location numbers until smallest number which maps to a seed is found
testLocationNum = 0
testing = True
lastUpdate = time.time()
while testing:
    #update console while program is running
    currenTime = time.time()
    if currenTime - lastUpdate > 1:
        os.system('cls')
        print(f"{testLocationNum} numbers tested!")
        lastUpdate = currenTime

    seedNumber = mapCascade.dest2source(testLocationNum)

    for range in seedRanges:
        if seedNumber in range:
            testing = False
            print(f"{testLocationNum} numbers tested!")
            print(f"Testing Done! The smallest location number corresponding to a seed is: {testLocationNum}")
    
    testLocationNum += 1
            