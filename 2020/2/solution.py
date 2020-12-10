file = open('data.txt', 'r')
data = [x.split() for x in file]

ctr = 0
ctr2 = 0
for entry in data:
	min_times, max_times = entry[0].split('-')
	letter = entry[1][0]
	password = entry[2]
	count = password.count(letter)
	if count >= int(min_times) and count <= int(max_times):
		ctr += 1

	if int(password[int(min_times)-1] == letter) + int(password[int(max_times)-1] == letter) == 1:
		ctr2+=1

print(ctr, ctr2)