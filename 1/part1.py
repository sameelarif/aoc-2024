leftLocations = []
rightLocations = []

with open('1/input.txt', 'r') as file:
    for line in file:
        locations = line.strip().split()
        leftLocations.append(int(locations[0]))
        rightLocations.append(int(locations[1]))

leftLocations.sort()
rightLocations.sort()

n = len(leftLocations)

totalDistance = 0

for i in range(n):
    totalDistance += abs(leftLocations[i] - rightLocations[i])

print(totalDistance)

