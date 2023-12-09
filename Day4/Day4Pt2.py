## DAY 4 PART 2 ##
import re

INPUT_FILE = 'input.txt'
#load and open file
input = open(INPUT_FILE,'r')
fileLines =  input.readlines()

cardPoints = 0
cardMultipliers = [1 for _ in range(len(fileLines))]
for index, cardSet in enumerate(fileLines):
    #get winning set
    winningSet = re.findall(r"\d+",re.search(r"(?:\d+\s+)+\|",cardSet).group())
    #get individual stes
    mySet = re.findall(r"\d+",re.search(r"\|(?:\s+\d+)+",cardSet).group())

    cardsToAdd = cardMultipliers[index]

    winningNumbers = len(list(set(winningSet) & set(mySet)))

    #add cards to subsequent cards
    for newIndex in range(index + 1, index + winningNumbers + 1): 
        cardMultipliers[newIndex] += cardsToAdd

print(f"Total Number of Cards: {sum(cardMultipliers)}")