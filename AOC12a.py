file = open("aoc 12 Input.txt", "r")

lines = file.readlines()
count = 0

for line in lines:
    num = ""
    for i,ch in enumerate(line):
        if ch.isdigit():
            if line[i-1] == "-":
                num = num + "-"
            num = num + ch
        elif not ch.isdigit() and num != "":
            count += int(num)
            num = ""

print(count)
file.close()