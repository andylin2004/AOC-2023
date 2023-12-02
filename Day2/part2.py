import re

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read()

ctr = 1
dict = {}

total = 0

for line in input.splitlines():
    line = line.split(": ")[1]
    items = re.split(", |; ", line)

    for word in items:
        info = word.split()
        if info[1] not in dict:
            dict[info[1]] = 0
        dict[info[1]] = max(int(info[0]), dict[info[1]])

    total += dict["red"] * dict["green"] * dict["blue"]

    dict.clear()
    ctr += 1

print(total)
