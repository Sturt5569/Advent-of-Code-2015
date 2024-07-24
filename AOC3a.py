file = open("aoc 3 Input.txt", 'r')

data = file.readlines()

nodes = [(0,0)]
posx,posy = 0,0

for line in data:
    for ch in line:
        match ch:
            case "^":
                posy += 1
            case "v":
                posy -= 1
            case ">":
                posx += 1
            case "<":
                posx -= 1
        if(posx,posy) not in nodes:
            nodes.append((posx,posy))
print(len(nodes))
file.close()