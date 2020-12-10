data_file = open('data.txt','r')

grid = dict()

x = y = 0

def p(x,y):
    if x not in grid:
        grid[x] = dict()

    if y not in grid[x]:
        grid[x][y] = 0

    grid[x][y] += 1

for line in data_file:
    for key in line:
        p(x,y)
        if key == ">":
            x +=1
        elif key == "^":
            y += 1
        elif key == "v":
            y -=1
        elif key == "<":
            x -=1

        p(x,y)


total = 0
for x in grid:
    for y in grid[x]:
        if grid[x][y] > 1:
            total += 1

print(total)

# 3.1

grid = dict()
ctr = 1
x = y = 0
x1 = y1 = 0
data_file = open('3.txt','r')
for line in data_file:
    for key in line:

        ctr += 1
        if ctr % 2 == 0:
            p(x,y)
            if key == ">":
                x +=1
            elif key == "^":
                y += 1
            elif key == "v":
                y -=1
            elif key == "<":
                x -=1
            p(x,y)
        else:
            p(x1,y1)
            if key == ">":
                x1 +=1
            elif key == "^":
                y1 += 1
            elif key == "v":
                y1 -=1
            elif key == "<":
                x1 -=1
            p(x1,y1)

total = 0
for x in grid:
    for y in grid[x]:
        if grid[x][y] > 1:
            total += 1

print(total)