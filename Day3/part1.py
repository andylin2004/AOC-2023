f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()
total = 0

for row in range(len(input)):
    adding = False
    numstr = ""
    for col in range(len(input[row])):
        if input[row][col].isnumeric():
            numstr += input[row][col]
            if not adding:
                if row > 0:
                    if col > 0:
                        if not input[row - 1][col - 1].isnumeric() and input[row - 1][col - 1] != ".":
                            adding = True
                        if not input[row - 1][col].isnumeric() and input[row - 1][col] != ".":
                            adding = True
                        if col < len(input[row]) - 1:
                            if not input[row - 1][col + 1].isnumeric() and input[row - 1][col + 1] != ".":
                                adding = True
                if col > 0:
                    if not input[row][col - 1].isnumeric() and input[row][col - 1] != ".":
                        adding = True
                if col < len(input[row]) - 1:
                    if not input[row][col + 1].isnumeric() and input[row][col + 1] != ".":
                        adding = True
                if row < len(input) - 1:
                    if col > 0:
                        if not input[row + 1][col - 1].isnumeric() and input[row + 1][col - 1] != ".":
                            adding = True
                        if not input[row + 1][col].isnumeric() and input[row + 1][col] != ".":
                            adding = True
                        if col < len(input[row]) - 1:
                            if not input[row + 1][col + 1].isnumeric() and input[row + 1][col + 1] != ".":
                                adding = True
            if col+1 >= len(input[row]) or not input[row][col + 1].isnumeric():
                print(numstr, adding)
                if adding:
                    total += int(numstr)
                numstr = ""
                adding = False
                    
print(total)