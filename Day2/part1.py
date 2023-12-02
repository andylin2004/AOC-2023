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

    if dict["red"] <= 12 and dict["green"] <= 13 and dict["blue"] <= 14:
        total += ctr

    dict.clear()
    ctr += 1

print(total)
