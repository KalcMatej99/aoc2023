
import numpy as np
with open('i', 'r') as file:
    content = file.read()

times = content.split("\n")[0].split(":")[1].strip().split(" ")
times = [x for x in times if x != ""]
times = "".join([str(t) for t in times])
times = [int(times)]

distances = content.split("\n")[1].split(":")[1].strip().split(" ")
distances = [x for x in distances if x != ""]
distances = "".join([str(t) for t in distances])
distances = [int(distances)]

print(times, distances)

def s_bis(s: int, speed:int, time:int, distance:int):
    print(s, speed)
    done_distance = (int(time) - speed) * speed
    if s == speed:
        if done_distance > distance:
            return s
        else:
            return None

    if done_distance > distance:
        mv = s_bis(s, s + int((speed - s)/2), time, distance)
    else:
        mv = s_bis(speed, speed + int((speed - s)/2), time, distance)

    if mv:
        return np.min([speed, mv])
    else:
        return speed

def e_bis(s:int, speed:int, time:int, distance:int):
    if s == speed:
        return s
    done_distance = (time - speed) * speed

    if done_distance > distance:
        mv = e_bis(speed, speed + int((speed - s)/2), time, distance)
    else:
        mv = e_bis(s, s + int((speed - s)/2), time, distance)

    return max([speed, mv])

ways_to_win_prod = 1
for time, distance in zip(times, distances):


    for speed in range(time):
        done_distance = (int(time) - speed) * speed

        if done_distance > int(distance):
            first_valid =speed
            break

    for speed in range(time - 1, 0, -1):
        done_distance = (int(time) - speed) * speed

        if done_distance > int(distance):
            last_valid =speed
            break

    print(first_valid, last_valid)
    ways_to_win_prod *= (last_valid - first_valid + 1)

print(ways_to_win_prod)