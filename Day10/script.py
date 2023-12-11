f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')

pipeMap = f.read().splitlines()
count = [[0 for _ in pipeMap[0]] for _ in pipeMap]

sLoc = None

for i in range(len(pipeMap)):
    for v in range(len(pipeMap[0])):
        if pipeMap[i][v] == "S":
            sLoc = (i, v)
            count[i][v] = 1
            break
    
    if sLoc is not None:
        break

curlocs = [sLoc]
visited = {sLoc}
startDirections = set()

exhausted = False

max_dist = 0

while not exhausted:
    newlocs = []
    possibleNext = 0
    for loc in curlocs:
        canNext = 0

        if pipeMap[loc[0]][loc[1]] == "S":
            if pipeMap[loc[0] - 1][loc[1]] in "|F7" and (loc[0] - 1, loc[1]) not in visited:
                visited.add((loc[0] - 1, loc[1]))
                count[loc[0] - 1][loc[1]] = max(count[loc[0]][loc[1]] +1, count[loc[0] - 1][loc[1]])
                newlocs.append((loc[0] - 1, loc[1]))
                max_dist = max(max_dist, count[loc[0] - 1][loc[1]])
                canNext += 1
                startDirections.add("up")

            if pipeMap[loc[0] + 1][loc[1]] in "|LJ" and (loc[0] + 1, loc[1]) not in visited:
                visited.add((loc[0] + 1, loc[1]))
                count[loc[0] + 1][loc[1]] = max(count[loc[0]][loc[1]] + 1, count[loc[0] + 1][loc[1]])
                newlocs.append((loc[0] + 1, loc[1]))
                max_dist = max(max_dist, count[loc[0] + 1][loc[1]])
                canNext += 1
                startDirections.add("down")

            if pipeMap[loc[0]][loc[1] - 1] in "-FL" and (loc[0], loc[1] - 1) not in visited:
                visited.add((loc[0], loc[1] - 1))
                count[loc[0]][loc[1] - 1] = max(count[loc[0]][loc[1]] +1, count[loc[0]][loc[1] - 1])
                newlocs.append((loc[0], loc[1] - 1))
                max_dist = max(max_dist, count[loc[0]][loc[1] - 1])
                canNext += 1
                startDirections.add("left")

            if pipeMap[loc[0]][loc[1] + 1] in "-J7" and (loc[0], loc[1] + 1) not in visited:
                visited.add((loc[0], loc[1] + 1))
                count[loc[0]][loc[1] + 1] = max(count[loc[0]][loc[1]] + 1, count[loc[0]][loc[1] + 1])
                newlocs.append((loc[0], loc[1] + 1))
                max_dist = max(max_dist, count[loc[0]][loc[1] + 1])
                canNext += 1
                startDirections.add("right")
            
            pipeMap[loc[0]].replace("S", "|")
        else:
            curIcon = pipeMap[loc[0]][loc[1]]

            if curIcon == "|":
                check = {"up", "down"}
            elif curIcon == "-":
                check = {"left", "right"}
            elif curIcon == "L":
                check = {"up", "right"}
            elif curIcon == "7":
                check = {"down", "left"}
            elif curIcon == "F":
                check = {"right", "down"}
            elif curIcon == "J":
                check = {"up", "left"}

            # print(loc, check)

            if "up" in check:
                if 0 <= loc[0] - 1 and pipeMap[loc[0] - 1][loc[1]] in "|F7" and (loc[0] - 1, loc[1]) not in visited:
                    visited.add((loc[0] - 1, loc[1]))
                    count[loc[0] - 1][loc[1]] = max(count[loc[0]][loc[1]] +1, count[loc[0] - 1][loc[1]])
                    newlocs.append((loc[0] - 1, loc[1]))
                    max_dist = max(max_dist, count[loc[0] - 1][loc[1]])
                    canNext += 1

            if "down" in check:
                if loc[0] + 1 < len(pipeMap) and pipeMap[loc[0] + 1][loc[1]] in "|LJ" and (loc[0] + 1, loc[1]) not in visited:
                    visited.add((loc[0] + 1, loc[1]))
                    count[loc[0] + 1][loc[1]] = max(count[loc[0]][loc[1]] + 1, count[loc[0] + 1][loc[1]])
                    newlocs.append((loc[0] + 1, loc[1]))
                    max_dist = max(max_dist, count[loc[0] + 1][loc[1]])
                    canNext += 1

            if "left" in check:
                if 0 <= loc[1] - 1 and pipeMap[loc[0]][loc[1] - 1] in "-FL" and (loc[0], loc[1] - 1) not in visited:
                    visited.add((loc[0], loc[1] - 1))
                    count[loc[0]][loc[1] - 1] = max(count[loc[0]][loc[1]] +1, count[loc[0]][loc[1] - 1])
                    newlocs.append((loc[0], loc[1] - 1))
                    max_dist = max(max_dist, count[loc[0]][loc[1] - 1])
                    canNext += 1

            if "right" in check:
                # print("eew")
                if loc[1] + 1 < len(pipeMap[0]) and pipeMap[loc[0]][loc[1] + 1] in "-J7" and (loc[0], loc[1] + 1) not in visited:
                    visited.add((loc[0], loc[1] + 1))
                    count[loc[0]][loc[1] + 1] = max(count[loc[0]][loc[1]] + 1, count[loc[0]][loc[1] + 1])
                    newlocs.append((loc[0], loc[1] + 1))
                    max_dist = max(max_dist, count[loc[0]][loc[1] + 1])
                    canNext += 1

        if canNext != 0:
            possibleNext += 1
    
    if possibleNext == 0:
        exhausted = True

    # print(newlocs)
    curlocs = newlocs

print("p1", max_dist)

total_in = 0

for row in range(len(pipeMap)):
    inside = False
    for col in range(len(pipeMap[0])):
        if (row, col) in visited and  pipeMap[row][col] in "|LJ":
            inside = not inside
        elif inside and count[row][col] == 0:
            total_in += 1

print(total_in)