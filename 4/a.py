# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the entire contents of the file
    content = file.read()
    

lines = content.split("\n")

c = [1] * len(lines)

sum_ = 0
for row_index, line in enumerate(lines):
    parts = line.split("|")

    winning = parts[0].split(":")[1].strip().split(" ")
    winning = set([x for x in winning if x != ""])
    my = parts[1].strip().split(" ")
    my = set([x for x in my if x != ""])

    print(winning, my)

    won = my.intersection(winning)
    n_matches = len(won)

    print(n_matches, 2 ** (n_matches - 1))

    if n_matches > 0:
        sum_ += 2 ** (n_matches - 1)

    for i in range(1, n_matches + 1):
        c[row_index + i] += c[row_index]
print(sum_)
print(sum(c))