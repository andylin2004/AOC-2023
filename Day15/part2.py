def hash(seq):
    curVal = 0
    for char in seq:
        if char in "-=":
            return curVal
        curVal += ord(char)
        curVal *= 17
        curVal %= 256
    return curVal


f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().split(",")

curVal = 0
total = 0

boxes = [[] for _ in range(256)]
box_loc = {}

for seq in input:
    value = None
    boxid = None
    pendingValue = False
    for char in seq:
        if pendingValue:
            value = int(char)
            if boxid in box_loc:
                new_box_info = (box_loc[boxid][0], value)
                old_box_val = box_loc[boxid][1]
                box_loc[boxid] = new_box_info
                if boxid == "tbxjmh":
                    print(boxes[173])
                    print(value)
                
                boxes[new_box_info[0]][boxes[new_box_info[0]].index((boxid, old_box_val))] = (boxid, value)
                if boxid == "tbxjmh":
                    print(boxes[173])
            else:
                box_slot = hash(boxid)
                boxes[box_slot].append((boxid, value))
                box_loc[boxid] = (box_slot, value)
        elif char not in "-=":
            curVal += ord(char)
            curVal *= 17
            curVal %= 256
        elif char == "=":
            pendingValue = True
            boxid = seq[:-2]
        elif char == "-":
            boxid = seq[:-1]
            if boxid in box_loc:
                box_slot_value = box_loc[boxid]
                boxes[box_slot_value[0]].remove((boxid, box_slot_value[1]))
                del box_loc[boxid]

total = 0

for i in range(len(boxes)):
    for v in range(len(boxes[i])):
        total += (i+1) * (v+1) * boxes[i][v][1]

print(total)
    
