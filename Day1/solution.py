left_list = []
right_list = []

with open('/Users/akshatkalra/Desktop/AdventOfCode/Day1/data.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

sorted_left = sorted(left_list)
sorted_right = sorted(right_list)


similarity = 0
for i in range(len(sorted_left)):
    occurance = 0
    for j in range(len(sorted_right)):
        if sorted_left[i] == sorted_right[j]:
            occurance += 1
    similarity += sorted_left[i] * occurance
    
print(similarity)