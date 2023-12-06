f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
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
mapping_ranked[0].reverse()
current_mapping = []

# print(mapping_ranked)

god_formulas = []

ctr = 0

for seed in mapping_ranked[0]:
    # print(seed)
    god_formulas_cur_lvl = [seed]
    # print()
    # print()
    # print(god_formulas_cur_lvl)

    for mappings in mapping_ranked[1:]:
        # print()
        god_formula_next = []
        for god_formula in god_formulas_cur_lvl:
            segments_done = []
            accounted_for = 0
            something_added = False
            for mapping in mappings:
                # print(seed, god_formulas_cur_lvl, mapping)
                # print(mappings[-1],"last mapping")
                if mapping[1] <= god_formula[0] < mapping[1] + mapping[2]:
                    new_interval = [god_formula[0] - (mapping[1] - mapping[0]), god_formula[1], min(god_formula[2], mapping[1]+ mapping[2] - god_formula[0])]
                    # print("new interval", new_interval)
                    god_formula_next.append(new_interval)
                    accounted_for += new_interval[2]
                    something_added = True
                    segments_done.append(new_interval[1])
                    segments_done.append(new_interval[2])
                elif mapping[1] < god_formula[0] + god_formula[2] < mapping[1] + mapping[2]:
                    new_interval = [mapping[0], mapping[1] - god_formula[0] + god_formula[1], god_formula[0] + god_formula[2] - mapping[1]]
                    god_formula_next.append(new_interval)
                    accounted_for += new_interval[2]
                    something_added = True
                    segments_done.append(new_interval[1])
                    segments_done.append(new_interval[2])
                elif god_formula[0] <= mapping[1] < god_formula[0] + god_formula[2]:
                    new_interval = [mapping[0], mapping[1] - god_formula[0] + god_formula[1], mapping[2]]
                    god_formula_next.append(new_interval)
                    accounted_for += new_interval[2]
                    something_added = True
                    segments_done.append(new_interval[1])
                    segments_done.append(new_interval[2])
                elif not something_added and mapping == mappings[-1]:
                    god_formula_next.append(god_formula)
                    accounted_for += god_formula[2]

            if accounted_for < god_formula[2]:
                if len(segments_done) > 0 and god_formula[1] < segments_done[0]:
                    new_interval = [god_formula[0], god_formula[1], segments_done[0] - god_formula[1]]
                    god_formula_next.append(new_interval)

                    for i in range(0, len(segments_done) - 2, 2):
                        if segments_done[i]+segments_done[i+1] != segments_done[i+2]:
                            new_interval = [segments_done[i]+segments_done[i+1] + god_formula[0] - god_formula[1], segments_done[i]+segments_done[i+1], segments_done[i+2] - (segments_done[i]+segments_done[i+1])]
                            god_formula_next.append(new_interval)

                    if segments_done[-2] + segments_done[-1] < god_formula[1] + god_formula[2]:
                        new_interval = [segments_done[-2]+segments_done[-1] + god_formula[0] - god_formula[1], segments_done[-2] + segments_done[-1], god_formula[1] + god_formula[2] - (segments_done[-2] + segments_done[-1])]
                        god_formula_next.append(new_interval)
                elif len(segments_done) > 0:
                    for i in range(0, len(segments_done) - 2, 2):
                        if segments_done[i]+segments_done[i+1] != segments_done[i+2]:
                            new_interval = [segments_done[i]+segments_done[i+1] + god_formula[0] - god_formula[1], segments_done[i]+segments_done[i+1], segments_done[i+2] - (segments_done[i]+segments_done[i+1])]
                            god_formula_next.append(new_interval)

                    if segments_done[-2] + segments_done[-1] < god_formula[1] + god_formula[2]:
                        new_interval = [segments_done[-2]+segments_done[-1] + god_formula[0] - god_formula[1], segments_done[-2] + segments_done[-1], god_formula[1] + god_formula[2] - (segments_done[-2] + segments_done[-1])]
                        god_formula_next.append(new_interval)
                else:
                    # print("not everything done yet")
                    new_interval = [god_formula[0] + god_formula_next[-1][2], god_formula_next[-1][1] + god_formula_next[-1][2], god_formula[2] - accounted_for]
                    god_formula_next.append(new_interval)
            
            # print(god_formula_next, "f")
        
        # print(sorted(god_formula_next, key=lambda x: (x[1])), "e")
        god_formulas_cur_lvl = god_formula_next

    god_formulas.extend(god_formulas_cur_lvl)
                
god_formulas.sort(key=lambda x: (x[0]))

print(god_formulas)

min_seed = None

for i in range(0, len(seed_ranges), 2):
    print(seed_ranges[i], seed_ranges[i+1])
    for range in god_formulas:
        print(min_seed)
        if seed_ranges[i] <= range[1] < seed_ranges[i] + seed_ranges[i+1]:
            print(seed_ranges[i], range)
            if min_seed is None:
                min_seed = range[0]
            else:
                min_seed = min(min_seed, range[0])
        elif range[1] <= seed_ranges[i] <= range[1]+range[2]:
            print(seed_ranges[i], range)
            if min_seed is None:
                min_seed = range[0]
            else:
                min_seed = min(min_seed, range[0])

print(min_seed)