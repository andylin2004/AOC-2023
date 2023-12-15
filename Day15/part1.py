f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().split(",")

curVal = 0
total = 0

for seq in input:
    for char in seq:
        curVal += ord(char)
        curVal *= 17
        curVal %= 256

    print(curVal)
    total += curVal
    curVal = 0
    

print(total)