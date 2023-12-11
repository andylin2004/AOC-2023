f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
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

stars = set()

for i in range(len(input)):
    for v in range(len(input[i])):
        if input[i][v] == "#":
            new_i = i
            new_v = v
            for row in additionalRows:
                if row < i:
                    new_i += 1000000 - 1
            for col in additionalCols:
                if col < v:
                    new_v += 1000000 - 1
            stars.add((new_i, new_v))

            print(i, v, new_i, new_v)

print(stars)

closestDistances = []
pairsAccounted = set()

for star in stars:
    for secondStar in stars:
        if star != secondStar and (star, secondStar) not in pairsAccounted and (secondStar, star) not in pairsAccounted:
            distance = abs(secondStar[1] - star[1]) + abs(secondStar[0] - star[0])
            pairsAccounted.add((star, secondStar))
            closestDistances.append(distance)

closestDistances.sort()
print(closestDistances)

print(sum(closestDistances))