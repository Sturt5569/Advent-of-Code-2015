file = open("aoc 3 Input.txt", 'r')

data = file.readlines()

nodes = [(0,0)]
santa_posx,santa_posy = 0,0
robo_posx,robo_posy = 0,0
turn = 0
for line in data:
    for ch in line:
        if turn == 0:
            match ch:
                case "^":
                    santa_posy += 1
                case "v":
                    santa_posy -= 1
                case ">":
                    santa_posx += 1
                case "<":
                    santa_posx -= 1
            if(santa_posx,santa_posy) not in nodes:
                nodes.append((santa_posx,santa_posy))
            turn = 1
            continue
        if turn == 1:
            match ch:
                case "^":
                    robo_posy += 1
                case "v":
                    robo_posy -= 1
                case ">":
                    robo_posx += 1
                case "<":
                    robo_posx -= 1
            if(robo_posx,robo_posy) not in nodes:
                nodes.append((robo_posx,robo_posy))
            turn = 0
            continue
print(len(nodes))
file.close()