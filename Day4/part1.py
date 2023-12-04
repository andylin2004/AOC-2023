f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

total = 0

for line in input:
    lcltotal = 0
    line = line.split(":")[1]
    line = line[1:]
    
    nums = line.split("|")

    winning = [int(x) for x in nums[0].split()]
    found = [int(x) for x in nums[1].split()]

    for num in found:
        if num in winning:
            if lcltotal == 0:
                lcltotal = 1
            else:
                lcltotal *= 2

    total += lcltotal

print(total)
