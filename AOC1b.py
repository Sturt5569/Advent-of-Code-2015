file = open("Advent of Code 2015/aoc 1 input.txt", 'r')

up = 0
down = 0
pos = 1
data = file.read()
for ch in data:

    if ch == "(":
        up += 1
    else:
        down += 1

    if up - down == -1:
        break
    pos += 1
    
print(pos)

file.close()