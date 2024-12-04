# Part 2
import re

with open('/Users/akshatkalra/Desktop/AdventOfCode/Day 3/data.txt', 'r') as file:
    data_string = file.read()


parsed = re.findall(r'mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)|do\(\)|don\'t\(\)', data_string)

filtered = []
enabled = True
for inst in parsed:
    if(re.search(r'mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)', inst)):
        if (enabled == True):
            filtered.append(inst)
    elif(re.search(r'do\(\)', inst)):
        enabled = True
    else:
        enabled = False




result = 0
for mul in filtered:
    to_multiply = re.findall(r'[0-9]?[0-9]?[0-9]', mul)
    result += int(to_multiply[0]) * int(to_multiply[1])
    
print(result)