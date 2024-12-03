with open('/Users/akshatkalra/Desktop/AdventOfCode/Day2/data.txt', 'r') as file:
    content = file.read()


lines = content.split('\n')
list = [line.split(' ') for line in lines]





def diff_check_with_one_allowed(list):
    global warning
    length = len(list)
    for i in range(length):
        if i == length - 1:
            return True
        if abs(int(list[i+1]) - int(list[i])) > 1 and abs(int(list[i+1]) - int(list[i])) <= 3:
            continue
        else:
            # if (warning == 0):
            #     warning = 1
            #     continue
            # else:
                return False

def all_increasing_or_decreasing(list):
    global warning
    inc = None
    if (int(list[1]) - int(list[0]) > 0):
        inc = True
    else:
        inc = False
        
    length = len(list)
    for i in range(length):
        if i == length - 1:
            return True
        if (inc and int(list[i+1]) - int(list[i]) > 0) or (not inc and int(list[i+1]) - int(list[i]) < 0):
            continue
        else:
            # if (warning == 0):
            #     warning = 1
            #     continue
            # else:
                return False
            
safe_reports = 0
warning = 0
for report in list:
    if (diff_check_with_one_allowed(report) and all_increasing_or_decreasing(report)):
        safe_reports += 1
        
print(safe_reports)
        
        
