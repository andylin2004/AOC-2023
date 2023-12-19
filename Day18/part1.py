f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().splitlines()

directions = [line.split()[:2] for line in input]

for i in range(len(directions)):
    directions[i][1] = int(directions[i][1])

verticies = []
curCoord = [0,0]
total = 0

for i in range(len(directions)):
    if directions[i][0] == "R":
        curCoord[1] += directions[i][1]
    elif directions[i][0] == "L":
        curCoord[1] -= directions[i][1]
    elif directions[i][0] == "U":
        curCoord[0] -= directions[i][1]
    elif directions[i][0] == "D":
        curCoord[0] += directions[i][1]

    total += directions[i][1]

    isNorth = (directions[i][0] == "D" and directions[(i+1) % len(directions)][0] in "LR") or (directions[(i+1) % len(directions)][0] == "U" and directions[i][0] in "LR")

    pointsRight = (directions[i][0] == "L" or directions[(i + 1) % len(directions)][0] == "R")

    verticies.append((curCoord[0], curCoord[1], isNorth, pointsRight))

print(verticies)

sortedVertical = sorted(verticies, key=lambda x: (x[0]))
sortedHoriz = sorted(verticies, key=lambda x: (x[1]))
        
print(sortedHoriz[0][1], sortedHoriz[-1][1])
print(sortedVertical[0][0], sortedVertical[-1][0])

grid = [[0 for _ in range(sortedHoriz[-1][1] - sortedHoriz[0][1] + 1)] for _ in range(sortedVertical[-1][0] - sortedVertical[0][0] + 1)]

cursor = [0-sortedVertical[0][0], 0-sortedHoriz[0][1]]

print(cursor)
for direction in directions:
    if direction[0] == "R":
        for _ in range(direction[1]):
            cursor[1] += 1
            grid[cursor[0]][cursor[1]] = 2
    elif direction[0] == "L":
        for _ in range(direction[1]):
            cursor[1] -= 1
            grid[cursor[0]][cursor[1]] = 2
    elif direction[0] == "U":
        for _ in range(direction[1]):
            cursor[0] -= 1
            grid[cursor[0]][cursor[1]] = 2
    elif direction[0] == "D":
        for _ in range(direction[1]):
            cursor[0] += 1
            grid[cursor[0]][cursor[1]] = 2

cursor = [0-sortedVertical[0][0], 0-sortedHoriz[0][1]]

instruction0 = directions[0]
instruction1 = directions[1]

for instruction in directions[:2]:
    if instruction[0] == "R":
        cursor[1] += 1
    elif instruction[0] == "L":
        cursor[1] -= 1
    elif instruction[0] == "U":
        cursor[0] -= 1
    elif instruction[0] == "D":
        cursor[0] += 1

cursors = set([tuple(cursor)])
found = set()

for row in grid:
    for item in row:
        if item:
            print("x", end="")
        else:
            print(" ", end="")

    print()

while len(cursors) > 0:
    print(cursors)
    next_cursors = set()
    for cursor in cursors:
        dxs = [0,1,0,-1]
        dys = [1,0,-1,0]

        for dx,dy in zip(dxs, dys):
            if (cursor[0]+dx, cursor[1]+dy) not in found and grid[cursor[0]+dx][cursor[1]+dy] == 0:
                grid[cursor[0]+dx][cursor[1]+dy] = 1
                found.add((cursor[0]+dx, cursor[1]+dy))
                next_cursors.add((cursor[0]+dx, cursor[1]+dy))

    cursors = next_cursors

print(len(found))
print(found)
for row in grid:
    for item in row:
        if item:
            print("x", end="")
        else:
            print(" ", end="")

    print()

print(len(found) + total)