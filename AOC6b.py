file = open("aoc 6 Input.txt", "r")

grid = [[0 for i in range(1000)] for j in range(1000)]

lines = file.readlines()

def switch(type,start,end):
    
    for i in range(int(start[0]),int(end[0]) + 1):
        for j in range(int(start[1]),int(end[1]) + 1):
            if type == 1:
                grid[i][j] += 2

            if type == 2:
                grid[i][j] += 1
            
            if type == 3:
                if grid[i][j] > 0:
                    grid[i][j] -= 1

for line in lines:
    if line.startswith("toggle"):
        line = line.split()
        start = tuple(line[1].split(sep=","))
        end = tuple(line[3].split(sep=","))

        switch(1,start,end)

    else:
        line = line.split()
        start = tuple(line[2].split(sep=","))
        end = tuple(line[4].split(sep=","))

        if line[1] == "on":
            switch(2,start,end)
        else:
            switch(3,start,end)

count = 0

for i in range(1000):
    for j in range(1000):
        count += grid[i][j]
        
print(count)
file.close()