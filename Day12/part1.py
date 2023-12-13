from collections import deque
import functools

clearedIt = set()

# @functools.lru_cache(maxsize=None)
def spring_eval(spring, broken, indx=0):
    if indx == len(spring):
        # print(spring)
        actually_broken = 0
        needs_broken = None
        in_zone = False

        for spring_element in spring:
            if spring_element == "#":
               actually_broken += 1
               if not in_zone:
                    in_zone = True
                    if len(broken) > 0:
                        needs_broken = broken.popleft()
                    else:
                        return 0
            else:
                if in_zone:
                    in_zone = False
                    if actually_broken != needs_broken:
                        return 0
                    
                    actually_broken = 0
                    needs_broken = None

        if len(broken) == 0 and (actually_broken == needs_broken or needs_broken is None):
            # print(spring)
            return 1
        return 0
    else:
        while indx < len(spring) and spring[indx] != "?":
            indx += 1

        if indx < len(spring) and spring[indx] == "?":
            left = spring.copy()
            right = spring.copy()
            left[indx] = "."
            right[indx] = "#"

        if indx >= len(spring):
            return spring_eval(spring, broken.copy(), indx)
        else:
            total = spring_eval(left, broken, indx)
            if right.count("#") <= sum(broken):
                total += spring_eval(right, broken, indx)

            return total

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.readlines()

broken_groupings = []
springs = []

for line in input:
    line = line.split()
    broken_groupings.append(deque(int(x) for x in line[1].split(",")))
    springs.append(deque(x for x in line[0]))

total_combo = 0

for (spring, broken_grouping, i) in zip(springs, broken_groupings, range(len(springs))):
    # print(i)
    # print(spring, "e")
    # print("".join(spring))
    total_combo += spring_eval(spring, broken_grouping)
    # print(clearedIt)
    clearedIt.clear()

print(total_combo)