import re

string = open('3/input.txt', 'r').read()
muls = re.findall(r'mul\(\d+,\d+\)', string)

total = 0

for mul in muls:
    x, y = mul.split(',')
    x = int(x[4:])
    y = int(y[:-1])

    total += x * y

print(total)
