import re
file = open("aoc 8 Input.txt", "r")

lines = file.readlines()

codecount = 0
memcount = 0

for line in lines:
    txt = line.rstrip("\n")
    codecount += (len(txt))
    txt = r"{}".format(txt)
    txt = txt.rstrip("\n")
    txt = txt.strip('"')
    txt = txt.replace(r"\"","1")
    txt = txt.replace(r"\\","1")
    txt = re.sub(r"\\x..", "9", txt)
    memcount += (len(txt))

print(codecount - memcount)

file.close()