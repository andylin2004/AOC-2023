from collections import deque

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

roundrocklocs = set()
cuberocklocs_updown = {}
cuberocklocs_lr = {}

# # print(input)

for i in range(len(input)):
    for v in range(len(input[0])):
        if input[i][v] == "O":
            roundrocklocs.add((i,v))
        elif input[i][v] == "#":
            if v not in cuberocklocs_updown:
                cuberocklocs_updown[v] = set()
            cuberocklocs_updown[v].add(i)
            if i not in cuberocklocs_lr:
                cuberocklocs_lr[i] = set()
            cuberocklocs_lr[i].add(v)

orderedStates = deque()

while len(orderedStates) == len(set(orderedStates)):
    movedroundrocklocs = set()
    for roundrockloc in roundrocklocs:
        # print(roundrockloc, "coords")
        if roundrockloc[1] not in cuberocklocs_updown:
            row = 0
            col = roundrockloc[1]

            while (row, col) in movedroundrocklocs:
                row += 1

            movedroundrocklocs.add((row, col))
        else:
            sortedcubes = sorted(cuberocklocs_updown[roundrockloc[1]])
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

            # print(mini, maxi, "e")
            
            while row > mini + 1:
                row -= 1

            while (row, col) in movedroundrocklocs:
                row += 1

            # print(row, col)
            movedroundrocklocs.add((row, col))

    roundrocklocs = movedroundrocklocs

    movedroundrocklocs = set()
    for roundrockloc in roundrocklocs:
        # print(roundrockloc, "coords")
        if roundrockloc[0] not in cuberocklocs_lr:
            row = roundrockloc[0]
            col = 0

            while (row, col) in movedroundrocklocs:
                col += 1

            movedroundrocklocs.add((row, col))
        else:
            sortedcubes = sorted(cuberocklocs_lr[roundrockloc[0]])
            i = 0
            mini = -1
            maxi = 0
            while i < len(sortedcubes) and sortedcubes[i] < roundrockloc[1]:
                mini = sortedcubes[i]
                if i >= len(sortedcubes) - 1:
                    maxi = len(input)
                else:
                    maxi = sortedcubes[i+1]
                i += 1
            
            row = roundrockloc[0]
            col = roundrockloc[1]

            # print(mini, maxi, "e")
            
            while col > mini + 1:
                col -= 1

            while (row, col) in movedroundrocklocs:
                col += 1

            # print(row, col)
            movedroundrocklocs.add((row, col))

    roundrocklocs = movedroundrocklocs

    movedroundrocklocs = set()
    for roundrockloc in roundrocklocs:
        # print(roundrockloc, "coords")
        if roundrockloc[1] not in cuberocklocs_updown:
            row = len(input)-1
            col = roundrockloc[1]

            while (row, col) in movedroundrocklocs:
                row -= 1

            movedroundrocklocs.add((row, col))
        else:
            sortedcubes = sorted(cuberocklocs_updown[roundrockloc[1]])
            i = len(sortedcubes) - 1
            mini = len(input[0])-1
            maxi = len(input[0])
            while i >= 0 and roundrockloc[0] < sortedcubes[i]:
                # print(i, "tbar")
                maxi = sortedcubes[i]
                if i <= 0:
                    mini = -1
                else:
                    mini = sortedcubes[i-1]
                i -= 1
            
            row = roundrockloc[0]
            col = roundrockloc[1]

            # print(mini, maxi, "e")
            
            while maxi - 1 > row:
                row += 1

            while (row, col) in movedroundrocklocs:
                row -= 1

            # print(row, col)
            movedroundrocklocs.add((row, col))

    roundrocklocs = movedroundrocklocs

    movedroundrocklocs = set()
    for roundrockloc in roundrocklocs:
        # print(roundrockloc, "coords")
        if roundrockloc[0] not in cuberocklocs_lr:
            row = roundrockloc[0]
            col = len(input[0])-1

            while (row, col) in movedroundrocklocs:
                col -= 1

            movedroundrocklocs.add((row, col))
        else:
            sortedcubes = sorted(cuberocklocs_lr[roundrockloc[0]])
            i = len(sortedcubes) - 1
            mini = len(input)-1
            maxi = len(input)
            while i >= 0 and roundrockloc[1] < sortedcubes[i]:
                # print(i, "tbar")
                maxi = sortedcubes[i]
                if i <= 0:
                    mini = -1
                else:
                    mini = sortedcubes[i-1]
                i -= 1
            
            row = roundrockloc[0]
            col = roundrockloc[1]

            # print(mini, maxi, "e")
            
            while maxi - 1 > col:
                col += 1

            while (row, col) in movedroundrocklocs:
                col -= 1

            # print(row, col)
            movedroundrocklocs.add((row, col))

    roundrocklocs = movedroundrocklocs

    orderedStates.append(tuple(roundrocklocs))


    # map = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
    # for coord in movedroundrocklocs:
    #     map[coord[0]][coord[1]] = 1

    # for row in map:
    #     for col in row:
    #         if col == 1:
    #             print(1, end="")
    #         else:
    #             print("x", end="")
    #     print()
    # print()

# orderedStates = orderedStates[:]
print(len(set(orderedStates)))
print(len((orderedStates)))
print(set(orderedStates))
print(orderedStates)

repeatsAt = 0

for i in range(len(orderedStates)):
    found = False
    for v in range(len(orderedStates)):
        if i == v:
            continue
        else:
            if orderedStates[i] == orderedStates[v]:
                repeatsAt = i
                found = True
                break

    if found:
        break

print(repeatsAt)

for _ in range(repeatsAt):
    orderedStates.popleft()

orderedStates.pop()

selected = orderedStates[(1000000000 - repeatsAt -1) % len(orderedStates)]

total = 0
for item in selected:
    total += len(input) - item[0]

print(total)