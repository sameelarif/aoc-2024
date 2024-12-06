input = open("4/input.txt", "r").read().split('\n')

directions = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]

n = len(input)
m = len(input[0])

word = "XMAS"
total = 0

def checkXmas(i, j, direction):
    for step in range(4):
        nextI = i + direction[0] * step
        nextJ = j + direction[1] * step

        if (nextI < 0 or nextI >= n or nextJ < 0 or nextJ >= m) or input[nextI][nextJ] != word[step]:
            return False
        
    return True

for i in range(n):
    for j in range(m):
        for direction in directions:
            if checkXmas(i, j, direction):
                total += 1

print(total)