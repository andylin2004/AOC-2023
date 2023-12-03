f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

gearratios = {}
total = 0

for row in range(len(input)):
    adding = False
    curgearcoord = None
    numstr = ""
    for col in range(len(input[row])):
        if input[row][col].isnumeric():
            numstr += input[row][col]
            if not adding:
                if row > 0:
                    if col > 0:
                        if not input[row - 1][col - 1].isnumeric() and input[row - 1][col - 1] == "*":
                            adding = True
                            curgearcoord = (row -1, col - 1)
                        if not input[row - 1][col].isnumeric() and input[row - 1][col] == "*":
                            adding = True
                            curgearcoord = (row - 1, col)
                        if col < len(input[row]) - 1:
                            if not input[row - 1][col + 1].isnumeric() and input[row - 1][col + 1] == "*":
                                adding = True
                                curgearcoord = (row - 1, col + 1)
                if col > 0:
                    if not input[row][col - 1].isnumeric() and input[row][col - 1] == "*":
                        adding = True
                        curgearcoord = (row, col -1)
                if col < len(input[row]) - 1:
                    if not input[row][col + 1].isnumeric() and input[row][col + 1] == "*":
                        adding = True
                        curgearcoord = (row, col+1)
                if row < len(input) - 1:
                    if col > 0:
                        if not input[row + 1][col - 1].isnumeric() and input[row + 1][col - 1] == "*":
                            adding = True
                            curgearcoord = (row+1, col-1)
                        if not input[row + 1][col].isnumeric() and input[row + 1][col] == "*":
                            adding = True
                            curgearcoord = (row+1, col)
                        if col < len(input[row]) - 1:
                            if not input[row + 1][col + 1].isnumeric() and input[row + 1][col + 1] == "*":
                                adding = True
                                curgearcoord = (row+1, col+1)
            if col+1 >= len(input[row]) or not input[row][col + 1].isnumeric():
                print(numstr, adding)
                if adding:
                    if curgearcoord not in gearratios:
                        gearratios[curgearcoord] = []
                    gearratios[curgearcoord].append(int(numstr))
                numstr = ""
                adding = False
                    
for gear in gearratios:
    if len(gearratios[gear]) == 2:
        total += gearratios[gear][0] * gearratios[gear][1]

print(total)