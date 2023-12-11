

with open('e', 'r') as file:
    content = file.read()


grid = content.split("\n")
grid_width = len(grid[0])
grid_height = len(grid)


index_start = [[i, row.index("S")] for i, row in enumerate(grid) if "S" in row][0]


current_pos = index_start
is_first = True

paths = [current_pos]


possible = []
next_move = []

# Move up
if current_pos[0] > 0:
    left_pos = [current_pos[0] - 1, current_pos[1]]

    left_elem = grid[left_pos[0]][left_pos[1]]

    if left_elem in ["|", "7", "F"]:
        possible.append(left_pos)

        if left_elem == "|":
            next_move.append(0)
        if left_elem == "7":
            next_move.append(3)
        if left_elem == "F":
            next_move.append(1)

# move right
if current_pos[1] < grid_width - 1:
    left_pos = [current_pos[0], current_pos[1] + 1]

    left_elem = grid[left_pos[0]][left_pos[1]]

    if left_elem in ["-", "7", "J"]:
        possible.append(left_pos)

        if left_elem == "-":
            next_move.append(1)
        if left_elem == "7":
            next_move.append(2)
        if left_elem == "J":
            next_move.append(0)

# move down
if current_pos[0] < grid_height - 1:
    left_pos = [current_pos[0] + 1, current_pos[1]]

    left_elem = grid[left_pos[0]][left_pos[1]]

    if left_elem in ["|", "L", "J"]:
        possible.append(left_pos)

        if left_elem == "|":
            next_move.append(2)
        if left_elem == "L":
            next_move.append(1)
        if left_elem == "J":
            next_move.append(3)

# move left
if current_pos[1] > 0:
    left_pos = [current_pos[0], current_pos[1] - 1]

    left_elem = grid[left_pos[0]][left_pos[1]]

    if left_elem in ["-", "L", "F"]:
        possible.append(left_pos)

        if left_elem == "-":
            next_move.append(3)
        if left_elem == "L":
            next_move.append(0)
        if left_elem == "F":
            next_move.append(2)


paths.append(possible[0].copy())

current_pos = possible[0]

next_move = next_move[0]

while current_pos != index_start:
    print(current_pos)
    if next_move == 0:
        current_pos[0] -= 1
    elif next_move == 1:
        current_pos[1] += 1
    elif next_move == 2:
        current_pos[0] += 1
    elif next_move == 3:
        current_pos[1] -= 1

    paths.append(current_pos.copy())

    new_elem = grid[current_pos[0]][current_pos[1]]

    if new_elem == "-":
        if next_move == 3:
            next_move = 3
        elif next_move == 1:
            next_move = 1
    elif new_elem == "|":
        if next_move == 0: next_move = 0
        elif next_move == 2: next_move = 2
    elif new_elem == "L":
        if next_move == 3: next_move = 0
        elif next_move == 2: next_move = 1
    
    elif new_elem == "F":
        if next_move == 0: next_move = 1
        elif next_move == 3: next_move = 2
    elif new_elem == "7":
        if next_move == 1: next_move = 2
        elif next_move == 0: next_move = 3
    elif new_elem == "J":
        if next_move == 2: next_move = 3
        elif next_move == 1: next_move = 0

print(paths)
print((len(paths) - 1)/2)

t_s = 0
for row_index in range(grid_height):
    graph_elems = [elem for elem in paths[:-1] if elem[0] == row_index]
    sorted_list = sorted(graph_elems, key=lambda x: x[1])
    print(sorted_list)

    s = 0
    for i, elem_in_row in enumerate(sorted_list[:-1]):
        if i % 2 != 0: continue
        next_elem = sorted_list[i + 1]

        d = next_elem[1] - elem_in_row[1] - 1

        print(next_elem, elem_in_row, d)

        s += d
    t_s += s

print(t_s)

