file = open('data.txt', 'r')
file_data = file.read()
groups_part1 = [set(x.replace('\n', '')) for x in file_data.split('\n\n')]

ctr = 0
for group in groups_part1:
    ctr += len(group)

print(ctr)


groups_part2 = [x.split('\n') for x in file_data.split('\n\n')]


ctr2 = 0
for group in groups_part2:
    for c in group[0]:
        if (all([c in g for g in group])):
            ctr2 +=1


print(ctr2)