from tqdm import tqdm

with open('i', 'r') as file:
    content = file.read()
    

def s1(content):
    seeds = content.split("\n")[0].split(":")[1].strip().split(" ")

    finals = []

    for seed in seeds:

        mut_seed = int(seed)

        for map_ in content.split(":")[1:]:
            rows = [x for x in map_.split("\n") if x != ""]
            rows = [word for word in rows if len(word.split(" ")) == 3]


            for row in rows:
                map_to = int(row.split(" ")[0])
                map_from = int(row.split(" ")[1])
                length = int(row.split(" ")[2])

                if mut_seed >= map_from and mut_seed < map_from + length:
                    mut_seed = mut_seed - map_from + map_to
                    break

        finals.append(mut_seed)

    print(min(finals))

def s2(content):

    def rec(s:int, e:int, maps: str, current_map:int = 0):

        if current_map >= len(maps):
            return s
        
        rows = [x for x in maps[current_map].split("\n") if x != ""]
        rows = [word for word in rows if len(word.split(" ")) == 3]

        mins = []

        for row in rows:
            map_to = int(row.split(" ")[0])
            map_from = int(row.split(" ")[1])
            length = int(row.split(" ")[2])

            if map_from <= s and map_from + length >= s and \
                map_from + length <= e:
                mins.append(rec(map_from + length + 1, e - 1, maps, current_map))
                mins.append(rec(s - map_from + map_to, length + map_to, maps, current_map + 1))
            
            elif s <= map_from and map_from <= e and e <= map_from + length:
                mins.append(rec(s, map_from - 1, maps, current_map))
                mins.append(rec(map_to, e - map_from + map_to, maps, current_map + 1))

            elif map_from >= s and map_from <= e and map_from + length >= s and map_from + length <= e:
                mins.append(rec(map_to, length + map_to, maps, current_map + 1))

                mins.append(rec(s, map_from - 1, maps, current_map))
                mins.append(rec(map_from + length + 1, e, maps, current_map))

            elif map_from <= s and map_from + length >= e:
                mins.append(rec(s - map_from + map_to, e - map_from + map_to, maps, current_map + 1))

        if len(mins) == 0:
            mins.append(rec(s, e, maps, current_map + 1))

        return min(mins)

    f_line = content.split("\n")[0].split(":")[1].strip().split(" ")
    seeds = f_line[::2]
    ranges = f_line[1::2]


    finals = []

    for seed, range in tqdm(zip(seeds, ranges), total=len(seeds)):

        maps = content.split(":")[2:]
        min_loc = rec(int(seed), int(seed) + int(range) - 1, maps, 0)
        finals.append(min_loc)

    print(min(finals))

s2(content)