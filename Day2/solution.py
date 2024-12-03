with open('/Users/akshatkalra/Desktop/AdventOfCode/Day2/data.txt', 'r') as file:
    content = file.read()


list = content.split('\n')


temp = list[0].split(' ')

warning = 0

def differ_check_with_one_allowed(list):
    global warning
    warning = 0
    length = len(list)
    for i in range(length):
        if i == length - 1:
            return True
        if abs(int(list[i+1]) - int(list[i])) >= 1 and abs(int(list[i+1]) - int(list[i])) <= 3:
            continue
        else:
            if (warning == 0):
                warning = 1
                continue
            return False

def all_increasing(list):
    global warning
    length = len(list)
    for i in range(length):
        if i == length - 1:
            return True
        if int(list[i+1]) - int(list[i]) >= 0:
            continue
        else:
            if (warning == 0):
                warning = 1
                continue
            return False

def all_decreasing(list):
    global warning
    length = len(list)
    for i in range(length):
        if i == length - 1:
            return True
        if int(list[i+1]) - int(list[i]) <= 0:
            continue
        else:
            if (warning == 0):
                warning = 1
                continue
            return False

safe_reports = 0
for report in list:
    parsed_report = report.split(' ')
    if (differ_check_with_one_allowed(parsed_report) and (all_increasing(parsed_report) or all_decreasing(parsed_report))):
        safe_reports += 1

print(safe_reports)