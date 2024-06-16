## DAY 6 PART 2 ##
import re
import math

INPUT_FILE = 'input.txt'
#load and open file
input = open(INPUT_FILE,'r')
fileLines =  input.readlines()

#retrieve race constraints
timeConstraint = ''.join(re.findall(r"(\d+)",fileLines[0]))
distanceRecord = ''.join(re.findall(r"(\d+)",fileLines[1]))

#use quadratic formula to find the roots of the movement function
timeLimit = int(timeConstraint)
distanceRec = int(distanceRecord)
roots = [
    (-1*timeLimit + math.sqrt(timeLimit**2 - 4*distanceRec))/(-2),
    (-1*timeLimit - math.sqrt(timeLimit**2 - 4*distanceRec))/(-2)
]

#sort roots in ascending order, round first root down and round second root up
roots.sort()
root1 = math.floor(roots[0])
root2 = math.ceil(roots[1])

print(f"Total Race Score: {len(range(root1 + 1, root2))}")
