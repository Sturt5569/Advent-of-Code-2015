import re
file = open("aoc 8 Input.txt", "r")

lines = file.readlines()

codecount = 0
memcount = 0

for line in lines:
    txt = line.rstrip("\n")
    codecount += (len(txt))
    txt = r"{}".format(txt)
    quotes = txt.count('"')
    slash = txt.count("\\")
    memcount += (len(txt) + quotes + slash + 2)


print(memcount - codecount)
file.close()