f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

seed_conversions = []

seed_conversions = [int(x) for x in input[0].split(':')[1].split()]
new_seed_conversions = [None] * len(seed_conversions)

for line in range(3, len(input)):
    print(input[line])
    if len(input[line]) > 0 and input[line][0].isnumeric():
        data = input[line].split()
        left_start = int(data[0])
        right_start = int(data[1])
        length = int(data[2])

        for i in range(len(seed_conversions)):
            if right_start <= seed_conversions[i] < right_start + length:
                new_seed_conversions[i] = left_start - right_start + seed_conversions[i]
    elif input[line] == "":
        for i in range(len(seed_conversions)):
            if new_seed_conversions[i] is not None:
                seed_conversions[i] = new_seed_conversions[i]
        
    print(new_seed_conversions, seed_conversions)
    
for i in range(len(seed_conversions)):
    if new_seed_conversions[i] is not None:
        seed_conversions[i] = new_seed_conversions[i]

print(min(seed_conversions))
