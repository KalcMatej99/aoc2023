import numpy as np
with open('e.txt', 'r') as file:
    content = file.read()

grid = [list(row) for row in content.split("\n")]

print(grid)

inf_rows = []
for i, row in enumerate(grid):
    if row.count("#") == 0:
        inf_rows.append(i)

inf_cols = []
print(np.transpose(grid))
for i, c in enumerate(np.transpose(grid)):
    print(c)
    if np.count_nonzero(c == '#') == 0:
        inf_cols.append(i)

print(inf_rows, inf_cols)


for i, r in enumerate(inf_rows):
    grid = np.insert(grid, r + i, ["."] * len(grid[0]), axis=0)

for i, r in enumerate(inf_cols):
    grid = np.insert(grid, r + i, ["."] * len(grid), axis=1)

print(grid)

indices = np.where(grid == '#')

print(indices)
indices = [(r, c) for r, c in zip(indices[0], indices[1])]
print(indices)

all_pairs = [(indices[i], indices[j]) for i in range(len(indices)) for j in range(i + 1, len(indices))]

print(all_pairs)

t_d = 0
for pair in all_pairs:

    start_column = min(pair[0][0], pair[1][0])
    end_column = max(pair[0][0], pair[1][0])

    empty_cols = 0

    '''for c in inf_cols:
        if c > start_column and c < end_column:
            empty_cols += 1'''


    start_row = min(pair[0][1], pair[1][1])
    end_row = max(pair[0][1], pair[1][1])

    empty_rows = 0

    '''for r in inf_rows:
        if r > start_row and r < end_row:
            empty_rows += 1'''

    d = np.abs(pair[0][0] - pair[1][0]) + empty_cols * 1 + \
        np.abs(pair[0][1] - pair[1][1]) + empty_cols * 1

    print(pair, d)

    t_d += d

print(t_d)