import itertools
file = open("aoc 9 Input.txt", "r")

lines = file.readlines()
paths = []
nodes = []
max_dist = 0

for line in lines:
    line = line.split()
    if line[0] not in nodes:
        nodes.append(line[0])
    if line[2] not in nodes:
        nodes.append(line[2])
    paths.append(line)

def get_path(route):
    distance = 0
    for i in range(len(route)-1):
        for path in paths:
            if route[i] in path and route[i+1] in path:
                distance += int(path[4])
    return distance

combinations = list(itertools.permutations(nodes,8))
for c in combinations:
    distance = get_path(c)
    if distance > max_dist:
        max_dist = distance

print(max_dist)
file.close()