leftLocations = []
rightLocations = []

with open('1/input.txt', 'r') as file:
    for line in file:
        locations = line.strip().split()
        leftLocations.append(int(locations[0]))
        rightLocations.append(int(locations[1]))

n = len(leftLocations)

frequencies = {}

for leftID in leftLocations:
    for rightID in rightLocations:
        if leftID not in frequencies:
            frequencies[leftID] = 0
        if rightID == leftID:
            frequencies[leftID] = frequencies.get(leftID, 0) + 1

leftLocations = [leftLocations[i] * frequencies[leftLocations[i]] for i in range(n)]

similarityScore = sum(leftLocations)

print(similarityScore)
