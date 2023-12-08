from math import lcm

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

mode = input[0]

nodes = {}
nodes_end_A = {}
nodes_end_Z = {}

for line in input[2:]:
    line = line.split()
    node_name = line[0]
    node_left = line[2][1:-1]
    node_right = line[3][:-1]

    nodes[node_name] = (node_left, node_right)

    if node_name[-1] == "A":
        nodes_end_A[node_name] = (node_left, node_right)

    if node_name[-1] == "Z":
        nodes_end_Z[node_name] = (node_left, node_right)

count_for_each_origin = []

for node in list(nodes_end_A.keys()):
    count = 0
    curNode = node
    while curNode[-1] != "Z":
        if mode[count % len(mode)] == "L":
            curNode = nodes[curNode][0]
        else:
            curNode = nodes[curNode][1]
        count += 1

    count_for_each_origin.append(count)

lcm_num = count_for_each_origin[0]

for num in count_for_each_origin[1:]:
    lcm_num = lcm(lcm_num, num)

print(lcm_num)