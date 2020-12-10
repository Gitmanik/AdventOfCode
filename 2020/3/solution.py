file = open('data.txt', 'r')
grid = []

for line in file:
	g = []
	for char in line:
		if char == '\n':
			continue
		g.append(char)
	grid.append(g)

def slope(delta_x, delta_y):
	x = y = 0
	ctr = 0
	while y < len(grid) - 1:
		x+=delta_x
		y+=delta_y
		c = grid[y][x % (len(grid[0]))]
		if c == '#':
			ctr += 1

	return ctr

print(slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2))