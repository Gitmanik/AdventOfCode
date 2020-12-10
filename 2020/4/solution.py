import re

file = open('data.txt', 'r')
file_str = file.read()


passports_data = [x.rsplit('\n') for x in file_str.split('\n\n')]
passports = []

for data in passports_data:
	p = dict()
	for entries in data:
		for entry in entries.split(' '):
			k,v = entry.split(':')
			p[k] = v

	passports.append(p)

ctr = 0
for passport in passports:
	if len(passport.keys()) == 8:
		ctr +=1
	elif len(passport.keys()) == 7 and 'cid' not in passport.keys():
		ctr +=1

part2 = 0

for p in passports:
	if len(p.keys()) != 8 and not (len(p.keys()) == 7 and 'cid' not in p.keys()):
		continue

	if int(p['byr']) not in range(1920, 2002 + 1):
		continue

	if int(p['iyr']) not in range(2010, 2020 + 1):
		continue

	if int(p['eyr']) not in range(2020, 2030 + 1):
		continue

	if len(p['pid']) != 9 or not p['pid'].isnumeric():
		continue

	if not any([x == p['ecl'] for x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']]):
		continue

	if not bool(re.match('^#[a-f0-9]{6}$', p['hcl'])):
		continue

	if not p['hgt'].endswith('cm') and not p['hgt'].endswith('in'):
		continue
	if (p['hgt'].endswith('cm') and int(p['hgt'][:-2]) not in range(150, 193+1)):
		continue
	if (p['hgt'].endswith('in') and int(p['hgt'][:-2]) not in range(59, 76+1)):
		continue

	part2 +=1

print(ctr, part2)