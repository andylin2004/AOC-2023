f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().splitlines()

additionalRows = set()
additionalCols = set()
for i in range(len(input)):
    if "#" not in input[i]:
        additionalRows.add(i)

for i in range(len(input[0])):
    string = "".join([input[x][i] for x in range(len(input))])

    if "#" not in string:
        additionalCols.add(i)

updatedGalaxy = []
for i in range(len(input)):
    resultStr = ""
    for v in range(len(input[0])):
        resultStr += input[i][v]
        if v in additionalCols:
            resultStr += "."
    updatedGalaxy.append(resultStr)
    if i in additionalRows:
        updatedGalaxy.append("." * (len(additionalCols) + len(input[0])))

# for line in updatedGalaxy:
#     print(line)

stars = set()
for i in range(len(updatedGalaxy)):
    for v in range(len(updatedGalaxy[0])):
        if updatedGalaxy[i][v] == "#":
            stars.add((i,v))

closestDistances = []
pairsAccounted = set()

for star in stars:
    for secondStar in stars:
        if star != secondStar and (star, secondStar) not in pairsAccounted and (secondStar, star) not in pairsAccounted:
            distance = abs(secondStar[1] - star[1]) + abs(secondStar[0] - star[0])
            pairsAccounted.add((star, secondStar))
            closestDistances.append(distance)

closestDistances.sort()

print(stars)
print(closestDistances)

print(sum(closestDistances))