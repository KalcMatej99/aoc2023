import numpy as np
import pandas as pd
with open('i', 'r') as file:
    content = file.read()

lines = content.split("\n")
hands = [line.split(" ")[0] for line in lines]
bids = [int(line.split(" ")[1]) for line in lines]

print(hands)

def char_to_int(c):
    if c == "J": return 0
    if c == "2": return 1
    if c == "3": return 2
    if c == "4": return 3
    if c == "5": return 4
    if c == "6": return 5
    if c == "7": return 6
    if c == "8": return 7
    if c == "9": return 8
    if c == "T": return 9
    if c == "Q": return 10
    if c == "K": return 11
    if c == "A": return 12
    
def hand_to_points(hand):
    return sum([13 ** (5 - i) * char_to_int(c) for i, c in enumerate(hand)])

def hand_to_type(hand):
    eval_hand = hand
    char_count = {}
    base = 15_000_000
    # Count occurrences of each character in the string
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    char_count = dict(sorted(char_count.items(), key=lambda item: -item[1]))

    keys = list(char_count.keys())

    if "J" in keys:
        if len(keys) == 1:
            keys = ["A"]
            del char_count["J"]
            char_count["A"] = 5
        else:
            keys.remove("J")
            char_count[keys[0]] += char_count["J"]
            del char_count["J"]
        


    if len(keys) == 1:
        return base * 6 + hand_to_points(eval_hand)
    if len(keys) == 2:
        if char_count[keys[0]] == 4:
            return base * 5 + hand_to_points(eval_hand)
        else:
            return base * 4 + hand_to_points(eval_hand)
    if len(keys) == 3:
        if char_count[keys[0]] == 3:
            return base * 3 + hand_to_points(eval_hand)
        else:
            return base * 2 + hand_to_points(eval_hand)
    if len(keys) == 4:
        return base * 1 + hand_to_points(eval_hand)

    return hand_to_points(eval_hand)
ranks = []

df = pd.DataFrame({"hands": hands, "bids": bids})
df["value"] = [hand_to_type(hand) for hand in df["hands"]]

df = df.sort_values(by= "value")

print(df)

res = sum([(i + 1) * bid for i, bid in enumerate(df["bids"])])

print(res)

del df["value"]
df.to_csv("c.csv", index = False)

from collections import Counter
order = 'J23456789TQKA'

L = [line.split() for line in open('i')]
L.sort(key=lambda x: [order.index(c) for c in x[0]])
L.sort(key=lambda x: max(sorted(Counter(x[0].replace('J', o)).values())[::-1] for o in order))
pd.DataFrame(L).to_csv("c2.csv", index = False)
print(sum(i * int(bid) for i, (_, bid) in enumerate(L, start=1)))