file = open("aoc 2 Input.txt", 'r')

data = file.readlines()
ribbon = 0

for line in data:
    line = line[:-1]
    sides = line.split(sep="x")
    bow = 1
    for i in range(len(sides)):
        sides[i] = int(sides[i])
        bow *= sides[i]
    sides.sort()
    ribbon += 2*sides[0] + 2*sides[1]
    ribbon += bow
    
print(ribbon)
file.close()