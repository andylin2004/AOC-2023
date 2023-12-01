import re

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read()

total = 0

for line in input.splitlines():

    f=re.finditer("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)

    e = [x.group(1) for x in f]

    print(line, e[0], e[-1])

    if e[0].isnumeric():
        total += int(e[0]) * 10
    elif e[0] == "one":
        total += 10
    elif e[0] == "two":
        total += 20
    elif e[0] == "three":
        total += 30
    elif e[0] == "four":
        total += 40
    elif e[0] == "five":
        total += 50
    elif e[0] == "six":
        total += 60
    elif e[0] == "seven":
        total += 70
    elif e[0] == "eight":
        total += 80
    elif e[0] == "nine":
        total += 90

    if e[-1].isnumeric():
        total += int(e[-1])
    elif e[-1] == "one":
        total += 1
    elif e[-1] == "two":
        total += 2
    elif e[-1] == "three":
        total += 3
    elif e[-1] == "four":
        total += 4
    elif e[-1] == "five":
        total += 5
    elif e[-1] == "six":
        total += 6
    elif e[-1] == "seven":
        total += 7
    elif e[-1] == "eight":
        total += 8
    elif e[-1] == "nine":
        total += 9

print(total)