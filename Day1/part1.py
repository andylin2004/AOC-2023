f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read()

total = 0

for line in input.splitlines():
    firstNum = None
    lastNum = None
    for char in line: 
        if firstNum is None and char.isnumeric():
            firstNum = int(char)
        if char.isnumeric():
            lastNum = int(char)
    
    print(firstNum, lastNum)
    if lastNum is None:
        total += firstNum
    else:
        total += firstNum * 10 + lastNum

print(total)
