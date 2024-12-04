#Part 1
import re

with open('/Users/akshatkalra/Desktop/AdventOfCode/Day 3/data.txt', 'r') as file:
    data_string = file.read()


parsed = re.findall(r'mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)', data_string)

# print (parsed)

result = 0
for mul in parsed:
    to_multiply = re.findall(r'[0-9]?[0-9]?[0-9]', mul)
    result += int(to_multiply[0]) * int(to_multiply[1])
    
print(result)