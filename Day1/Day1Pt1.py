## DAY 1 PART 1 ##
#load and open file
input = open('input.txt','r')

fileLines = [line.strip() for line in input.readlines()]

calValues = []
for line in fileLines:

    #get string of integers in each line
    calString = ''
    for char in line:
        try:
            int(char)
            calString += char
        except ValueError: pass
    
    #get list of integers made of of first and last integer in calString
    calValues.append(int(calString[0] + calString[-1]))

print(f"Sum of calibration values: {sum(calValues)}")