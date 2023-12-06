from math import ceil

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

times = [int(x) for x in input[0].split(":")[1].split()]
distances = [int(x) for x in input[1].split(":")[1].split()]

total = -1

for i in range(len(times)):
    lcltotal = 0
    minToBeat = distances[i]
    time = ceil((times[i] - 1)/2)
    if time % 2 == 1:
        left = time
        right = time + 1
    else:
        left = time
        right = time
    
    while (times[i] - left) * left > minToBeat or (times[i] - right) * right > minToBeat:
        print(left, right)
        if left != right:
            if (times[i] - left) * left > minToBeat:
                lcltotal += 1
        if (times[i] - right) * right > minToBeat:
                lcltotal += 1
        
        left -= 1
        right += 1

    if total == -1:
         total = lcltotal
    else:
         total *= lcltotal

    print()

print(total)