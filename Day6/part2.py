from math import ceil

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

total_times = int(input[0].split(":")[1].replace(" ", ""))
total_distances = int(input[1].split(":")[1].replace(" ", ""))

total = -1

lcltotal = 0
minToBeat = total_distances
time = ceil((total_times - 1)/2)
if time % 2 == 1:
    left = time
    right = time + 1
else:
    left = time
    right = time

print(left, right)

while (total_times - left) * left > minToBeat and (total_times - right) * right > minToBeat:
    # print(left, right)
    if left != right:
        if (total_times - left) * left > minToBeat:
            lcltotal += 1
            left -= 1
    if (total_times - right) * right > minToBeat:
        lcltotal += 1
        right += 1

while (total_times - left) * left > minToBeat:
    if (total_times - left) * left > minToBeat:
        lcltotal += 1
        left -= 1

while (total_times - right) * right > minToBeat:
    if (total_times - right) * right > minToBeat:
        lcltotal += 1
        right += 1

    
print(right - left - 1)

# 44899691
# 277113618901768