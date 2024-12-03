import re

string = open('3/input.txt', 'r').read()
commands = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', string)

total = 0
enabled = True

for command in commands:
    if command == "do()":
        enabled = True
    elif command == "don't()":
        enabled = False
    elif enabled and command.startswith("mul"):
        x, y = command[4:-1].split(',')

        x = int(x)
        y = int(y)
        
        total += x * y

print(total)
