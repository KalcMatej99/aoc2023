


with open('i', 'r') as file:
    content = file.read()

def get_next_number(numbers: list) -> int:
    

    step_list = []
    step_list.append(numbers)
    while any(step_list[-1]):
        this_step = []
        for i in range(len(step_list[-1][:-1])):
            this_step.append(step_list[-1][i+1] - step_list[-1][i])
        step_list.append(this_step)


    # Calculate the result
    result = 0
    step_list.reverse()
    for i in range(len(step_list)):
        result += step_list[i][-1]

    return result



def get_previous_number(numbers: list) -> int:
    
    step_list = []
    step_list.append(numbers)
    while any(step_list[-1]):
        this_step = []
        for i in range(len(step_list[-1][:-1])):
            this_step.append(step_list[-1][i+1] - step_list[-1][i])
        step_list.append(this_step)

    step_list.reverse()
    # Calculate the result
    result = 0
    for i in range(len(step_list)):
        result = step_list[i][0] - result
    return result

t_sum = 0
for line in content.split("\n"):
    next_elem = get_previous_number([int(e) for e in line.strip().split(" ")])
    print(line, next_elem)
    t_sum += next_elem
print(t_sum)