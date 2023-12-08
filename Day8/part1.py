f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

mode = input[0]

nodes = {}

for line in input[2:]:
    line = line.split()
    node_name = line[0]
    node_left = line[2][1:-1]
    node_right = line[3][:-1]

    nodes[node_name] = (node_left, node_right)

curNode = "AAA"
count = 0
while curNode != "ZZZ":
    if mode[count % len(mode)] == "L":
        curNode = nodes[curNode][0]
    else:
        curNode = nodes[curNode][1]
    count += 1

print(count)
