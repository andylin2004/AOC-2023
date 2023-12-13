f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
inputs = f.read().split("\n\n")

total = 0

for input in inputs:
    horizontalRows = input.split()

    vertical_rows = []

    for row in horizontalRows:
        print(row)

    for i in range(len(horizontalRows[0])):
        vertical_rows.append([horizontalRows[v][i] for v in range(len(horizontalRows))])

    for i in range(1, len(horizontalRows)):
        left = i - 1
        right = i
        mirrored = True
        while left >= 0 and right < len(horizontalRows) and mirrored:
            for (leftSym, rightSym) in zip(horizontalRows[left], horizontalRows[right]):
                if leftSym != rightSym:
                    mirrored = False
                    break
            left -= 1
            right += 1

        if mirrored:
            print(i, "e")
            total += (i) * 100

    print(horizontalRows[3], "haha")

    if mirrored:
        continue

    print(vertical_rows)
    for i in range(1, len(vertical_rows)):
        left = i - 1
        right = i
        mirrored = True
        while left >= 0 and right < len(vertical_rows) and mirrored:
            for (leftSym, rightSym) in zip(vertical_rows[left], vertical_rows[right]):
                if leftSym != rightSym:
                    mirrored = False
                    break
            left -= 1
            right += 1

        if mirrored:
            print(i, "f")
            total += i

print(total)