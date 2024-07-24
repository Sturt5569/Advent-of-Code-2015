file = open("aoc 7 Input.txt", "r")

lines = file.readlines()
wires = {}

run = True

def make_binary(num):
    val = '{0:016b}'.format(int(num))
    return val

def bin_not(input):
    output = ""
    for ch in input:
        if ch == "1":
            output = output + "0"
        else:
            output = output + "1"
    return output

def bin_and(input1, input2):
    output = ""
    for i in range(16):
        if input1[i] == "1" and input2[i] == "1":
            output = output + "1"
        else:
            output = output + "0"
    return output

def bin_or(input1, input2):
    output = ""
    for i in range(16):
        if input1[i] == "1" or input2[i] == "1":
            output = output + "1"
        else:
            output = output + "0"
    return output

def lshift(input, factor):
    input = list(input)
    for i in range(factor):
        input.append("0")
    output = "".join(input)
    return output[factor:]

def rshift(input, factor):
    input = list(input)
    for i in range(factor):
        input.insert(0,"0")
    output = "".join(input)
    return output[:16]

count = 0
while count < 350:
    
    count += 1
    for line in lines:
        line = line.split()
        if line[1] == "->":
            if line[0].isnumeric():
                wires[line[2]] = make_binary(line[0])
            else:
                if line[0] in wires.keys():
                    wires[line[2]] = wires.get(line[0])

        if line[0] == "NOT":
            if line[1] in wires.keys():
                wires[line[3]] = bin_not(wires.get(line[1]))
    
        if line[1] == "AND":
            if (line[0] in wires.keys() or line[0].isnumeric()) and (line[2] in wires.keys() or line[2].isnumeric()):
                if line[0].isnumeric():
                    input1 = make_binary(line[0])
                else:
                    input1 = wires.get(line[0])
                
                if line[2].isnumeric():
                    input2 = make_binary(line[2])
                else:
                    input2 = wires.get(line[2])

                wires[line[4]] = bin_and(input1,input2)

        if line[1] == "OR":
            if (line[0] in wires.keys() or line[0].isnumeric()) and (line[2] in wires.keys() or line[2].isnumeric()):
                if line[0].isnumeric():
                    input1 = make_binary(line[0])
                else:
                    input1 = wires.get(line[0])
                
                if line[2].isnumeric():
                    input2 = make_binary(line[2])
                else:
                    input2 = wires.get(line[2])
                wires[line[4]] = bin_or(input1,input2)

        if line[1] == "LSHIFT":
            if line[0] in wires.keys():
                wires[line[4]] = lshift(wires.get(line[0]),int(line[2]))

        if line[1] == "RSHIFT":
            if line[0] in wires.keys():
                wires[line[4]] = rshift(wires.get(line[0]),int(line[2]))
                
print(int(wires.get("a"),2))

file.close()