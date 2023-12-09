from collections import deque

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

total = 0

for line in input:
    layers = deque()
    
    layers.append([int(x) for x in line.split()])

    while True:
        new_layer = []
        for i in range(len(layers[-1]) - 1):
            new_layer.append(layers[-1][i+1] - layers[-1][i])

        layers.append(new_layer)

        if set(new_layer) == {0}:
            break

    while len(layers) > 1:
        # print(layers)
        last_layer = layers.pop()
        layers[-1].append(last_layer[-1] + layers[-1][-1])

    # print(layers)
    total += layers[-1][-1]      
    # print()     
    
print(total)