## DAY 3 PART 1 ##
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
engineScore = 0

for y, row in enumerate(dataFrame):
   #get coordinates for all numbers
   numMatches = [(match.group(),[(x,y) for x in range(*match.span())]) for match in re.compile(r"\d+").finditer(row)]

   for match in numMatches:
      number, coords = match
      neighbors = get_adjacent_indices(coords,cols,rows)

      #loop through all neighboring coordinates to find any non '.' symbols
      for x,y in neighbors:
         neighbor = dataFrame[y][x]

         if re.match(r"[^\d\.]", neighbor):
            engineScore += int(number)
            break

print(f"Total Engine Score: {engineScore}")