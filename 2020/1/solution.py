data_file = open('data.txt', 'r')

data = [int(x.rstrip('\n')) for x in data_file]

for x in data:
	for y in data:
		if x + y == 2020:
			print(x*y)

for x in data:
	for y in data:
		for z in data:
			if x + y + z == 2020:
				print(x*y*z)