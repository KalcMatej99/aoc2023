import numpy as np
import pandas as pd
with open('i', 'r') as file:
    content = file.read()

mov = content.split("\n")[0].strip()

nodes = {}

for line in content.split("\n")[2:]:
    name = line.split("=")[0].strip()

    left = line.split("=")[1].strip().split(",")[0][1:].strip()
    right = line.split("=")[1].strip().split(",")[1][:-1].strip()

    nodes[name] = {}
    nodes[name]["L"] = left
    nodes[name]["R"] = right

c_nodes = [name for name in nodes.keys() if name.endswith("A")]
print(c_nodes)

steps_all = []
for c_node in c_nodes:
    steps = 0
    while not c_node.endswith("Z"):
        for movement in mov:
            c_node = nodes[c_node][movement]
            steps += 1
    steps_all.append(steps)

print(steps_all)
print(np.lcm.reduce(steps_all))