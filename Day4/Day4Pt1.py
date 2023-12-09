## DAY 4 PART 1 ##
import re

INPUT_FILE = 'input.txt'
#load and open file
input = open(INPUT_FILE,'r')
fileLines =  input.readlines()

cardPoints = 0
for cardSet in fileLines:
    #get winning set
    winningSet = re.findall(r"\d+",re.search(r"(?:\d+\s+)+\|",cardSet).group())
    #get individual stes
    mySet = re.findall(r"\d+",re.search(r"\|(?:\s+\d+)+",cardSet).group())

    winningNumbers = len(list(set(winningSet) & set(mySet)))

    if winningNumbers != 0: cardPoints += 2**(winningNumbers - 1)

print(f"Sum of Scratcard Points: {cardPoints}")