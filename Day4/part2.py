f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

total = 0
eachwinning = []
instances = []

for line in input:
    lcltotal = 0
    line = line.split(":")[1]
    line = line[1:]
    
    nums = line.split("|")

    winning = [int(x) for x in nums[0].split()]
    found = [int(x) for x in nums[1].split()]

    for num in found:
        if num in winning:
            lcltotal += 1

    eachwinning.append(lcltotal)
    instances.append(1)

# print(eachwinning)

for i in range(len(eachwinning)):
    # print(i)
    for v in range(eachwinning[i]):
        instances[i + v + 1] += 1 * instances[i]
    # print(instances)
    
# print(instances)
total = sum(instances)

print(total)