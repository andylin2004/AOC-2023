from collections import deque
from functools import cache

cached = {}

def spring_eval(spring, cur_broken, indx=0, num_hash=0, seg_start=0):
    # print(spring, cur_broken, indx, num_hash, seg_start)

    if (spring[seg_start:], cur_broken) in cached:
        return cached[(spring[seg_start:], cur_broken)]
    
    if indx >= len(spring):
        if len(cur_broken) == 0 and num_hash == 0:
            # print("yay")
            return 1
        else:
            # print("oof")
            return 0
    
    if spring[indx] == "#":
        if len(cur_broken) == 0 or (num_hash == 0 and indx-1 >= 0 and spring[indx-1] == "#" and seg_start != indx + 1):
            return 0
        else:
            num_hash += 1
    elif spring[indx] == "?":
        # print("hehe")
        if num_hash == 0 and indx > 0 and spring[indx-1] == "#":
            # print(spring, "####!!!")
            spring = spring.replace("?", ".", 1)

            result = spring_eval(spring, cur_broken, indx + 1, num_hash, indx+1)

            cached[(spring[indx+1:], cur_broken[1:])] = result

            return result
        else:
            left = spring.replace("?", "#", 1)
            right = spring.replace("?", ".", 1)
            # print(left, right)

            return spring_eval(left, cur_broken, indx, num_hash, seg_start) + spring_eval(right, cur_broken, indx, num_hash, seg_start)
    elif spring[indx] == ".":
        if num_hash > 0:
            return 0
        
    if len(cur_broken) > 0 and cur_broken[0] == num_hash:
        result = spring_eval(spring, cur_broken[1:], indx+1, 0, indx+1)

        cached[(spring[indx+1:], cur_broken[1:])] = result

        return result
    else:
        return spring_eval(spring, cur_broken, indx+1, num_hash, seg_start)

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.readlines()

broken_groupings = []
springs = []

for line in input:
    line = line.split()
    broken_groupings.append(tuple(int(x) for x in line[1].split(",") * 5))
    springs.append(((line[0] + "?") * 5)[:-1])
    # broken_groupings.append(tuple(int(x) for x in line[1].split(",")))
    # springs.append(line[0])

total_combo = 0

for (spring, broken_grouping, i) in zip(springs, broken_groupings, range(len(springs))):
    
    e = spring_eval(spring, broken_grouping)
    # print(spring, e)
    total_combo += e
    cached.clear()
    # print(total_combo)

print(total_combo)