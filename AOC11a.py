inp = list("vzbxkghb")
alphabet = "abcdefghijklmnopqrstuvwxyz"
banned = ["i","o","l"]

def increment(inp,n=0):
    output = inp
    if output[len(output)-n-1] == "z":
        output[len(output)-n-1] = "a"
        output = increment(output,n+1)
    else:
        output[len(output)-n-1] = chr(ord(output[len(output)-n-1])+1)

    return output

def test(inp):
    const = False
    pairs = False
    for ch in banned:
        if ch in inp:
            return False
        
    trio = ["",inp[0],inp[1]]
    for i in range(2,len(inp)):
        trio.pop(0)
        trio.append(inp[i])
        check = "".join(trio)
        if check in alphabet:
            const = True
            break
    doubles = []
    pair = ["",""]
    for i in range(len(inp)):
        pair.pop(0)
        pair.append(inp[i])
        if pair[0] == pair[1]:
            paired = "".join(pair)
            if paired not in doubles:
                doubles.append(paired)
        if len(doubles) >= 2:
            pairs = True
            break
    
    if pairs and const:
        return True
    else:
        return False


run = True
while run:
    inp = increment(inp)
    if test(inp):
        run = False

print("".join(inp))