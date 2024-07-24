file = open("aoc 5 Input.txt", 'r')

data = file.readlines()

nice = 0

for line in data:
    pairs = False
    middle = False

    for i in range(len(line)-1):
        test = line[i] + line[i+1]
        if line.find(test,i+2) != -1:
            pairs = True
        
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            middle = True
    
    if pairs and middle:
        nice += 1
       
print(nice)
file.close()