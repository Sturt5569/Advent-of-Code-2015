inp = "1321131112"

def process(num):
    count = 0
    newstring = ""
    for i in range(len(num)):
        count += 1
        if i == len(num)-1:
            res = str(count) + num[i]
            newstring = newstring + res
            count = 0
        elif num[i] != num[i+1]:
            res = str(count) + num[i]
            newstring = newstring + res
            count = 0
        else:
            continue
    return newstring

for i in range(40):
    inp = process(inp)

print(len(inp))