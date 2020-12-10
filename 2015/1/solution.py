file = open('data.txt', 'r')
data = file.read()
floor = 0
basement = 0

for l in range(0,len(data)):
    x = data[l]
    if x == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1 and basement == 0:
        basement = l + 1

print(floor, basement)