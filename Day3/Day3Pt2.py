## DAY 3 PART 2 ##
import re

INPUT_FILE = 'input.txt'
#load and open file
input = open(INPUT_FILE,'r')
fileLines = [line.strip() for line in input.readlines()]
   
def get_adjacent_indices(coords:list, graphWidth:int, graphHeight:int) -> list:
   """takes in a list of coords making up a string, and finds all coords adjacent to those coords"""
   neighbors = []

   for x, y in coords:
      for delX in [-1,0,1]:
         for delY in [-1,0,1]:
            newX = x + delX
            newY = y + delY

            if newX < 0 or newY < 0 or newX > graphWidth-1 or newY > graphHeight-1: continue

            if (newX,newY) not in coords and (newX,newY) not in neighbors: 
               neighbors.append((newX,newY))
   
   return neighbors

#load and open as dataframe
dataFrame = [line for line in fileLines]

#iterate through all items in dataframe
rows = len(dataFrame)
cols = len(dataFrame[0])
ratioSum = 0

#find all numbers in document with corresponding coordinates
numMatches = []
for y, row in enumerate(dataFrame):
   numMatches += [(match.group(),[(x,y) for x in range(*match.span())]) for match in re.compile(r"\d+").finditer(row)]

   
#find two coordinates contained in numbers neighboring a gear
gearNeighbors = []
for y, row in enumerate(dataFrame):
   #get x coordinates for all non '.' symbols
   xVals = [match.span()[0] for match in re.compile(r"[^\d\.]").finditer(row)]
   
   for x in xVals:
      #for each symbol, find all neighboring coordinates that have a number in them
      neighbors = get_adjacent_indices([(x,y)],cols,rows)
      numberNeighbors = [(x,y) for x,y in neighbors if re.match(r"\d",dataFrame[y][x])]

      #iterate through all matched numbers
      gearNumbers = []
      for number, coordList in numMatches:
         #if any coordinate in that number is in numberNeighbors, add it to gearNumbers
         intersection = list(set(coordList) & set(numberNeighbors))
         if len(intersection) != 0: gearNumbers.append(int(number))
      
      if len(gearNumbers) == 2: 
         ratioSum += gearNumbers[0] * gearNumbers[1]

print(f"Sum of gear ratios: {ratioSum}")