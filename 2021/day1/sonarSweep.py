
lines = [x for x in open('input.txt', 'r').readlines()]

#PART 1
previousValue = 0
counter = 0
for value in lines:
    value = int(value)
    if previousValue != 0 and previousValue < value:
        counter += 1
    previousValue = value
print(counter)

#PART 2
def windowCalculator(arr):
    result = 0
    for measurment in arr:
        result += int(measurment)
    return result

counter = 0
for i in range(0, len(lines)):
    if (i+3 < len(lines) and lines[i+3] != ''):
        firstWindow = [lines[i], lines[i+1], lines[i+2]]
        secondWindow = [lines[i+1], lines[i+2], lines[i+3]]
        firstWindowResult = windowCalculator(firstWindow)
        secondWindowResult = windowCalculator(secondWindow)
        if (firstWindowResult < secondWindowResult):
            counter += 1
        
print(counter)