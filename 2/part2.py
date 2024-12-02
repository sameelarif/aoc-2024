reports = []

with open('2/input.txt', 'r') as file:
    for line in file:
        reports.append([int(x) for x in line.strip().split()])
safeCount = 0

for report in reports:
    direction = report[1] - report[0]
    isSafe = True
    breakingLevels = 0

    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3):
            breakingLevels += 1

            if breakingLevels > 1:
                isSafe = False
                break

        if (direction > 0 and report[i] >= report[i + 1]) or (direction < 0 and report[i] <= report[i + 1]):
            breakingLevels += 1
            
            if breakingLevels > 1:
                isSafe = False
                break

    safeCount += int(isSafe)

print(safeCount)
