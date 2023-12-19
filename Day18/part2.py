f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

directions = [line.split()[2] for line in input]

verticies = []
curCoord = [0,0]
perimTotal = 0

for i in range(len(directions)):
    hex = directions[i]
    direction = int(hex[-2])
    firstFive = hex[2:-2]

    intMove = int(firstFive, base=16)
    
    print(intMove)

    if direction == 0:
        curCoord[1] += intMove
    elif direction == 2:
        curCoord[1] -= intMove
    elif direction == 3:
        curCoord[0] -= intMove
    elif direction == 1:
        curCoord[0] += intMove

    perimTotal += intMove

    verticies.append((curCoord[0], curCoord[1]))

verticies.reverse()
print(verticies)

total = 0

for i in range(len(verticies)):
    total += verticies[i][0] * verticies[(i+1) % len(verticies)][1] - verticies[(i+1) % len(verticies)][0] * verticies[i][1]
    print(i, (i+1) % len(verticies))

print((total +perimTotal) / 2 +1)