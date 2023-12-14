f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().splitlines()

roundrocklocs = set()
cuberocklocs = {}

print(input)

for i in range(len(input)):
    for v in range(len(input[0])):
        if input[i][v] == "O":
            roundrocklocs.add((i,v))
        elif input[i][v] == "#":
            if v not in cuberocklocs:
                cuberocklocs[v] = set()
            cuberocklocs[v].add(i)

movedroundrocklocs = set()

for roundrockloc in roundrocklocs:
    print(roundrockloc, "coords")
    if roundrockloc[1] not in cuberocklocs:
        row = 0
        col = roundrockloc[1]

        while (row, col) in movedroundrocklocs:
            row += 1

        movedroundrocklocs.add((row, col))
    else:
        sortedcubes = sorted(cuberocklocs[roundrockloc[1]])
        i = 0
        mini = -1
        maxi = 0
        while i < len(sortedcubes) and sortedcubes[i] < roundrockloc[0]:
            mini = sortedcubes[i]
            if i >= len(sortedcubes) - 1:
                maxi = len(input)
            else:
                maxi = sortedcubes[i+1]
            i += 1
        
        row = roundrockloc[0]
        col = roundrockloc[1]

        print(mini, maxi, "e")
        
        while row > mini + 1:
            row -= 1

        while (row, col) in movedroundrocklocs:
            row += 1

        print(row, col)
        movedroundrocklocs.add((row, col))

print(movedroundrocklocs)

map = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]

for coord in movedroundrocklocs:
    map[coord[0]][coord[1]] = 1

for row in map:
    for col in row:
        if col == 1:
            print(1, end="")
        else:
            print(" ", end="")
    print()

total = 0
for item in movedroundrocklocs:
    total += len(input[0]) - item[0]

print(total)