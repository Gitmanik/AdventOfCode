import math, sys

file = open('data.txt', 'r')

y_min = 0
y_max = 127

x_min = 0
x_max = 7

seatID_max = 0

seats = []

for seat in file:
	sy_min = y_min
	sy_max = y_max

	sx_min = x_min
	sx_max = x_max 

	for c in seat:
		if c == 'F':
			sy_max = math.floor((sy_min + sy_max) / 2)
		if c == 'B':
			sy_min = math.ceil((sy_min + sy_max) / 2)

		if c == 'L':
			sx_max = math.floor((sx_min + sx_max) / 2)
		if c == 'R':
			sx_min = math.ceil((sx_min + sx_max) / 2)

	seatID = sy_min * 8 + sx_min

	seats.append((sx_min, sy_min, seatID))
	seatID_max = max(seatID, seatID_max)

print(seatID_max)

z = [x[2] for x in seats]
z.sort()

for ctr in range(len(z) - 1):
	if z[ctr] + 1 != z[ctr+1]:
		print(z[ctr] + 1)

