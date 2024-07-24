file = open("aoc 12 Input.txt", "r")

lines = file.readlines()
count = 0

for line in lines:
    num = ""
    nest = [0]
    nest_level = 0
    red = False
    for i,ch in enumerate(line):
        if ch == "{":
            nest_level += 1
            nest.append(0)
            print(nest)
        if ch == "}" and red == False:
            if nest_level > 0:
                nest[nest_level-1] += nest[nest_level]
                del nest[nest_level]
                nest_level -= 1
                print(nest)
            else:
                count += nest[nest_level]
                del nest[nest_level]
                print(nest)

        if ch == "}" and red == True:
                del nest[nest_level]
                nest_level -= 1

        if ch.isdigit():
            if line[i-1] == "-":
                num = num + "-"
            num = num + ch
        elif not ch.isdigit() and num != "":
            nest[nest_level] += int(num)
            num = ""

print(count)
file.close()