def sort_by_power(cards):
    # print(cards)
    inventory = {}
    for card in cards:
        if card not in inventory:
            inventory[card] = 0
        inventory[card] += 1

    if "J" in inventory:
        if inventory["J"] == 5:
            inventory["A"] = 5
            del inventory["J"]
        else:
            no_j = inventory.copy()
            del no_j["J"]
            inventory[max(list(no_j.keys()), key=lambda x: (no_j[x]))] += inventory["J"]
            del inventory["J"]

    print(sorted(list(inventory.values())))
    # high
    if len(inventory) == 5:
        return 1
    # one
    elif len(inventory) == 4:
        return 2
    # two
    elif len(inventory) == 3 and sorted(list(inventory.values())) == [1, 2, 2]:
        return 3
    # three of a kind
    elif len(inventory) == 3 and sorted(list(inventory.values())) == [1, 1, 3]:
        return 4
    # full house
    elif len(inventory) == 2 and sorted(list(inventory.values())) == [2,3]:
        return 5
    # four of a kind
    elif len(inventory) == 2 and sorted(list(inventory.values())) == [1,4]:
        return 6
    # five of a kind
    elif len(inventory) == 1:
        return 7
    
def card_converter(card):
    if card.isnumeric():
        return int(card)
    elif card == "T":
        return 10
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    elif card == "J":
        return 1
    
f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

cards_bids = []

for card_bid in input:
    card_bid = card_bid.split()
    card_bid[1] = int(card_bid[1])

    cards_bids.append(card_bid)

print(cards_bids)

# e = [card_bid[0] for card_bid in cards_bids]
# print(len(e), len(set(e)))

for card_bid in cards_bids:
    print(card_bid, sort_by_power(card_bid[0]))

cards_bids.sort(key=lambda x: (sort_by_power(x[0]), card_converter(x[0][0]), card_converter(x[0][1]), card_converter(x[0][2]), card_converter(x[0][3]), card_converter(x[0][4])))

print(cards_bids)

total = 0
for i in range(len(cards_bids)):
    total += (i+1) * cards_bids[i][1]

print(total)