# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the entire contents of the file
    content = file.read()
    

lines = content.split("\n")

import re

def find_number_indices(input_string):
    # Using regular expression to find all numbers and their indices
    pattern = re.compile(r'\d+')
    matches = pattern.finditer(input_string)

    # Storing indices of numbers in a list of tuples (index, number)
    indices = [(match.start(), match.group()) for match in matches]
    return indices

def find_non_number_period_indices(input_string):
    # Using regular expression to find all indices where characters are neither numbers nor periods
    pattern = re.compile(r'[^0-9\.]')
    matches = pattern.finditer(input_string)

    # Storing indices where characters are neither numbers nor periods
    indices = [match.start() for match in matches]
    return indices

def find_stars_indices(input_string):
    return [index for index, char in enumerate(input_string) if char == '*']

all_valid_numbers = {}
sum_numbers = 0
for i in range(len(lines)):
    all_valid_numbers[i] = {}

    valid_numbers = []
    line = lines[i]
    print(line)
    number_indices = find_number_indices(line)

    character_indices = find_non_number_period_indices(line)

    if i > 0:
        character_indices.extend(find_non_number_period_indices(lines[i - 1]))

    if i < len(lines) - 1:
        character_indices.extend(find_non_number_period_indices(lines[i + 1]))

    for index, value in number_indices:

        start_index = index - 1
        end_index = index + len(str(value))

        for special_char_index in character_indices:
            if special_char_index >= start_index and special_char_index <= end_index:
                valid_numbers.append(int(value))
                all_valid_numbers[i][index] = int(value)
                break
        
    print(valid_numbers)

    sum_numbers += sum(valid_numbers)

print()
sum_gear = 0
for i in range(1, len(lines) - 1):
    line = lines[i]
    stars_indices = find_stars_indices(line)

    print("i", stars_indices)

    for star_index in stars_indices:
        top_left = (i - 1, star_index - 3)
        top_right = (i - 1, star_index + 1)
        bottom_left = (i + 1, star_index - 3)
        bottom_right = (i + 1, star_index + 1)

        two_vals = []
        stop = False
        for row_i in range(i - 1, i + 2):
            if stop: break
            for column_index in range(star_index - 3, star_index + 2):
                if stop: break
                if column_index in all_valid_numbers[row_i]:
                    n = all_valid_numbers[row_i][column_index]
                    if column_index >= star_index - 3 and len(str(n)) == 3 or column_index >= star_index - 2 and len(str(n)) == 2 or column_index >= star_index - 1:
                        two_vals.append(all_valid_numbers[row_i][column_index])
                        if len(two_vals) == 2:
                            print(two_vals)
                            sum_gear += two_vals[0] * two_vals[1]
                            two_vals = []
                            stop = True
                            break


print(sum_numbers, sum_gear)

