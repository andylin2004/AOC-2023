f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().splitlines()

seed_conversions = []

mapping_ranked = []

current_mapping = []

seed_ranges = [int(x) for x in input[0].split(':')[1].split()]

for i in range(0, len(seed_ranges), 2):
    seed_conversions.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i+1]))

for line in input[3:]:
    if len(line) > 0 and line[0].isnumeric():
        current_mapping.append([int(x) for x in line.split()])
    elif len(line) == 0:
        current_mapping.sort(key=lambda x: (x[1]))
        mapping_ranked.append(current_mapping)
        current_mapping = []

current_mapping.sort(key=lambda x: (x[1]))
mapping_ranked.append(current_mapping)
current_mapping = []

print(mapping_ranked)

god_formulas = []

ctr = 0

for seed in mapping_ranked[0]:
    god_formulas_cur_lvl = [seed]
    print()
    print(god_formulas_cur_lvl)

    for mappings in mapping_ranked[1:]:
        god_formula_next = []
        for god_formula in god_formulas_cur_lvl:
            remaining = god_formula[2]
            for mapping in mappings:
                print(mapping, "current_mapping", god_formula, "cur_god")
                if mapping[1] <= god_formula[0] < mapping[1] + mapping[2]:
                    nextGod = [god_formula[0] - (mapping[1] - mapping[0]), god_formula[1], min(mapping[1] + mapping[2] - god_formula[0], god_formula[2])]
                    remaining -= nextGod[2]

                    god_formula_next.append(nextGod)
                    print(god_formula_next, "aaa")
                # elif god_formula[1] <= mapping[1] < god_formula[1] + god_formula[2]:
                #     nextGod = [mapping[1] - (mapping[1] - mapping[0]), god_formula[0], min(mapping[1] + mapping[2] - god_formula[0], god_formula[2])]
                #     remaining -= nextGod[2]
                #     god_formula_next.append(nextGod)
                #     print(god_formula_next, "bbb")
                elif god_formula[0] < mapping[1] < god_formula[0] + god_formula[2] and remaining - nextGod[2] > 0:
                    nextGod = [mapping[0], mapping[1] + mapping[2] - god_formula[0] + god_formula[1], nextGod[2]]
                    remaining -= nextGod[2]
                    god_formula_next.append(nextGod)
                    # nextGod = [mapping[0], mapping[1], remaining]
                    # god_formula_next.append(nextGod)
                    # remaining = 0
                    print(god_formula_next, "ccc")
            
            if remaining > 0:
                sorted_for_func = sorted(god_formula_next, key = lambda x: (x[1]))
                print(god_formula_next, "eee")

                for i in range(len(sorted_for_func) - 1):
                    if sorted_for_func[i][1] + sorted_for_func[i][2] != sorted_for_func[i + 1][1]:
                        nextGod = [god_formula[0], sorted_for_func[i][1] + sorted_for_func[i][2], sorted_for_func[i+1][1] - (sorted_for_func[i][1] + sorted_for_func[i][2])]

                        remaining -= sorted_for_func[i+1][1] - (sorted_for_func[i][1] + sorted_for_func[i][2])
                        god_formula_next.append(nextGod)

                if god_formula[2] != remaining and remaining > 0:
                    nextGod = [god_formula[0] + god_formula[2] - remaining, sorted_for_func[len(sorted_for_func) - 1][1] + sorted_for_func[len(sorted_for_func) - 1][2], remaining]
                    god_formula_next.append(nextGod)
                elif len(god_formula_next) == 0 or (god_formula[0], god_formula[1]) != (god_formula_next[len(god_formula_next) - 1][0], god_formula_next[len(god_formula_next) - 1][1]):
                    god_formula_next.append(god_formula)

                print(god_formula_next, "fff")

        god_formulas_cur_lvl = god_formula_next
    
    god_formulas.extend(god_formulas_cur_lvl)
    print(god_formulas_cur_lvl)



print(god_formulas)



# result = []

# for formula in god_formulas:
#     for seed_range in seed_conversions:
#         if seed_range[0] <= formula[1] < seed_range[1]:
#             result.append(formula[1] - (formula[1] - formula[0]))
#         elif formula[1] <= seed_range[0] < formula[1] + formula[2]:
#             result.append(seed_range[0] - (formula[1] - formula[0]))
#         elif formula[1] <= seed_range[1] < formula[1]:
#             result.append(formula[0])

# print(result)

# nextGod = [god_formula[0] - (best_next_mapping[1] - best_next_mapping[0]), god_formula[1] + accounted_for, min(best_next_mapping[1] + best_next_mapping[2] - god_formula[0], god_formula[2]) - accounted_for]

# if map[1] <= god_formula[0] + accounted_for < map[1] + map[2]: