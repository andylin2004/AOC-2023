import heapq

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
array = f.read().splitlines()

array = [[int(x) for x in row] for row in array]

# print(array)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dij(array): #dijkastra algo for pathcounting

    # three arrays
    results = [[[[10000 for _ in range(4)] for _ in range(4)] for _ in range(len(array[0]))] for _ in range(len(array))] # for keeping the least number of steps to get to an array slot
    isVisited = [[[[False for _ in range(4)] for _ in range(4)] for _ in range(len(array[0]))] for _ in range(len(array))] # one for keeping track of if we already determined the least number of steps to get to an array slot
    pq = [] # for keeping track of next min slot to go to

    pq.append([0, (0,0), (0,0)]) # preprocessing start place so we can kickstart checking the neighbors later
    results[0][0] = [[0] * 4] * 4 # preprocessing the start, as it doesn't count at all and we don't want anything bad to happen

    heapq.heapify(pq) # dijkstra uses a priority queue

    while len(pq) > 0:
        u = heapq.heappop(pq) # pop out the thing in the array where the tentative (first indice) value is the least of all of them, because we are very sure that is the min
        # # print(u)
        x = u[1][0]
        y = u[1][1]
        x_ctr = u[2][0]
        y_ctr = u[2][1]
        # if isVisited[x][y]: # just in case it pops up again sometime later and we already did it with a better case scenario
        #     continue
        for cx,cy in zip(dx,dy):
            if 0 <= x+cx < len(array) and 0 <= y+cy < len(array[0]):
                # print("\n", u, sep="")

                dir = 0
                if x_ctr < 0:
                    dir = 0
                elif x_ctr > 0:
                    dir = 1
                elif y_ctr < 0:
                    dir = 2
                elif y_ctr > 0:
                    dir = 3

                if 0 <= dir <= 1 and 0 <= abs(x_ctr) <= 3:
                    newDist = results[x][y][dir][abs(x_ctr)]
                elif 2 <= dir <= 3 and 0 <= abs(y_ctr) <= 3:
                    newDist = results[x][y][dir][abs(y_ctr)]
                else:
                    # print(x_ctr, y_ctr, cx, cy, "noped 1st")
                    continue

                # print(newDist, "aha")
                newDist += array[x+cx][y+cy] # newDist is the tentative distance plus the number at a neighbor specified

                if x_ctr * cx >= 0 and y_ctr * cy >= 0:
                    if cy == 1:
                        dir = 3
                    elif cy == -1:
                        dir = 2
                    elif cx == 1:
                        dir = 1
                    elif cx == -1:
                        dir = 0
                else:
                    # print(x_ctr, y_ctr, cx, cy, "noped 1.5st")
                    continue

                if 0 <= dir <= 1 and 0 <= abs(x_ctr+cx)<= 3:
                    checkMax = (x+cx, y+cy, dir, abs(x_ctr+cx))
                    # print("max", checkMax)
                elif 2 <= dir <= 3 and 0 <= abs(y_ctr+cy)<= 3:
                    checkMax = (x+cx, y+cy, dir, abs(y_ctr+cy))
                    # print("max", checkMax)
                else:
                    # print(x_ctr, y_ctr, cx, cy, "noped 1.7st")
                    continue


                # print(results[checkMax[0]][checkMax[1]][checkMax[2]][checkMax[3]])
                if results[checkMax[0]][checkMax[1]][checkMax[2]][checkMax[3]] > newDist: # we want the least num of steps to the neighbor as possible, so keep the min of the two for the tentative result
                    # print(x_ctr, y_ctr, cx, cy)
                    if 0 <= abs(x_ctr) < 3 and abs(cx) == 1 and x_ctr * cx >= 0:
                        # # print(x_ctr, "x")
                        results[checkMax[0]][checkMax[1]][checkMax[2]][checkMax[3]] = newDist
                        heapq.heappush(pq, [newDist, (x+cx, y+cy), (x_ctr + cx, 0)]) # we will handle the neighbor's neighbors later, once we are more sure that this is the min it can go
                    elif 0 <= abs(y_ctr) < 3 and abs(cy) == 1 and y_ctr * cy >= 0:
                        # # print(y_ctr, "y")
                        results[checkMax[0]][checkMax[1]][checkMax[2]][checkMax[3]] = newDist
                        heapq.heappush(pq, [newDist, (x+cx, y+cy), (0, y_ctr+cy)]) # we will handle the neighbor's neighbors later, once we are more sure that this is the min it can go

                    if 0 <= dir <= 1:
                        isVisited[x][y][dir][abs(x_ctr+cx)] = True
                    elif 2 <= dir <= 3:
                        isVisited[x][y][dir][abs(y_ctr+cy)] = True
                    # print(pq)
                # else:
                #     # print(x_ctr, y_ctr, cx, cy, "noped 2nd")

        # # print(results)
        # for row in results:
        #     # print(row)
        # # print()

        # print("", end="")

    return min(min(results[-1][-1]))

print(dij(array))