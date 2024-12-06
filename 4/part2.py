input = open("4/input.txt", "r").read().split('\n')

count = 0
n = len(input)
m = len(input[0])

def inBounds(x, y):
    return 0 <= x < n and 0 <= y < m

def checkPattern(x, y):
    if not inBounds(x, y) or input[x][y] != 'A':
        return False

    checks = [
        ((x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)),
        ((x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y - 1)),
        ((x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)),
        ((x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1))
    ]

    for check in checks:
        if (inBounds(check[0][0], check[0][1]) and input[check[0][0]][check[0][1]] == 'M' and
            inBounds(check[1][0], check[1][1]) and input[check[1][0]][check[1][1]] == 'S' and
            inBounds(check[2][0], check[2][1]) and input[check[2][0]][check[2][1]] == 'M' and
            inBounds(check[3][0], check[3][1]) and input[check[3][0]][check[3][1]] == 'S'):
            return True

    return False
    
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if checkPattern(i, j):
            count += 1

print(count)