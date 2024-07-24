file = open("aoc 5 Input.txt", 'r')

data = file.readlines()

nice = 0

aeiou = list("aeiou")
letters = ["ab","cd","pq","xy"]

for line in data:
    vowels = 0
    double = False
    invalid = False

    for lets in letters:
        if lets in line:
            invalid = True
            
    if invalid == True:
        continue

    base = 0
    for ch in line:
        if ch in aeiou:
            vowels += 1
        if ch == base:
            double = True
        base = ch
        
    if vowels >= 3 and double == True:
        nice += 1
        
print(nice)
file.close()