file = open('example.txt', 'r')

lines = [int(x.rstrip('\n')) for x in file]

l = 5

def check(last, expected):
    print(last, expected)
    for x in last:
        for y in last:
            if x+y == expected:
                print(x,y,expected)
                return True


    return False


for i in range(l, len(lines) - 1):
    if not check(lines[i-l:i], lines[i+1]):
        print(i,lines[i+1])
        break