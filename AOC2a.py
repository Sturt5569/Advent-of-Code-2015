file = open("aoc 2 Input.txt", 'r')

data = file.readlines()
area = 0

for line in data:
    line = line[:-1]
    sides = line.split(sep="x")
    for i in range(len(sides)):
        sides[i] = int(sides[i])
    
    faces = [sides[0]*sides[1],sides[0]*sides[2],sides[1]*sides[2]]
    faces.sort()
    area += 2*faces[0] + 2*faces[1] + 2*faces[2] + faces[0]
        
print(area)
file.close()