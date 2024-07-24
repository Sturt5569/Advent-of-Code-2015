file = open("Advent of Code 2015/aoc 1 input.txt", 'r')

up = 0
down = 0

for line in file:
    up += line.count("(")
    down += line.count(")")
    print(up-down)

file.close()