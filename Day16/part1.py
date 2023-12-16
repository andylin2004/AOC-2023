f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

energized = [["" for _ in input[0]] for _ in input]
beamInfos = [[0,0,"r", []]]

while len(beamInfos) > 0:
    new_locs = []
    for beamInfo in beamInfos:
        if input[beamInfo[0]][beamInfo[1]] == "\\":
            if beamInfo[2] == "r":
                if beamInfo[0] + 1 < len(input):
                    new_locs.append([beamInfo[0] + 1, beamInfo[1], "d", beamInfo[3]])
            elif beamInfo[2] == "l":
                if 0 <= beamInfo[0] - 1:
                    new_locs.append([beamInfo[0]  - 1, beamInfo[1], "u", beamInfo[3]])
            elif beamInfo[2] == "u":
                if 0 <= beamInfo[1] - 1:
                    new_locs.append([beamInfo[0], beamInfo[1] - 1, "l", beamInfo[3]])
            elif beamInfo[2] == "d":
                if beamInfo[1] + 1 < len(input[0]):
                    new_locs.append([beamInfo[0], beamInfo[1] + 1, "r", beamInfo[3]])
        
        elif input[beamInfo[0]][beamInfo[1]] == "/":
            if beamInfo[2] == "r":
                if 0 <= beamInfo[0] - 1:
                    new_locs.append([beamInfo[0] - 1, beamInfo[1], "u", beamInfo[3]])
            elif beamInfo[2] == "l":
                if beamInfo[0] + 1 < len(input):
                    new_locs.append([beamInfo[0] + 1, beamInfo[1], "d", beamInfo[3]])
            elif beamInfo[2] == "u":
                if beamInfo[1] + 1 < len(input[0]):
                    new_locs.append([beamInfo[0], beamInfo[1] + 1, "r", beamInfo[3]])
            elif beamInfo[2] == "d":
                if 0 <= beamInfo[1] - 1:
                    new_locs.append([beamInfo[0], beamInfo[1] - 1, "l", beamInfo[3]])

        elif input[beamInfo[0]][beamInfo[1]] == "|" and beamInfo[2] in "lr":
            if "l" not in energized[beamInfo[0]][beamInfo[1]] and "r" not in energized[beamInfo[0]][beamInfo[1]]:
                if 0 <= beamInfo[0] - 1:
                    new_locs.append([beamInfo[0] - 1, beamInfo[1], "u", beamInfo[3].copy()])
                if beamInfo[0] + 1 < len(input):
                    new_locs.append([beamInfo[0] + 1, beamInfo[1], "d", beamInfo[3].copy()])
        
        elif input[beamInfo[0]][beamInfo[1]] == "-" and beamInfo[2] in "ud":
            if "u" not in energized[beamInfo[0]][beamInfo[1]] and "d" not in energized[beamInfo[0]][beamInfo[1]]:
                if 0 <= beamInfo[1] - 1:
                    new_locs.append([beamInfo[0], beamInfo[1] - 1, "l", beamInfo[3].copy()])
                if beamInfo[1] + 1 < len(input[0]):
                    new_locs.append([beamInfo[0], beamInfo[1] + 1, "r", beamInfo[3].copy()])

        else:
            if beamInfo[2] == "r":
                if beamInfo[1] + 1 < len(input[0]):
                    new_locs.append([beamInfo[0], beamInfo[1] + 1, beamInfo[2], beamInfo[3]])
            elif beamInfo[2] == "l":
                if 0 <= beamInfo[1] - 1:
                    new_locs.append([beamInfo[0], beamInfo[1] - 1, beamInfo[2], beamInfo[3]])
            elif beamInfo[2] == "u":
                if 0 <= beamInfo[0] - 1:
                    new_locs.append([beamInfo[0] - 1, beamInfo[1], beamInfo[2], beamInfo[3]])
            elif beamInfo[2] == "d":
                if beamInfo[0] + 1 < len(input):
                    new_locs.append([beamInfo[0] + 1, beamInfo[1], beamInfo[2], beamInfo[3]])

        energized[beamInfo[0]][beamInfo[1]] += beamInfo[2]
    beamInfos = new_locs


total = 0
for row in energized:
    for col in row:
        if len(col) > 0:
            total += 1
    #         print("X", end="")
    #     else:
    #         print(" ", end="")
    # print()

print(total)