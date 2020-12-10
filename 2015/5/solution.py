file_data = open('data.txt', 'r')

data = [x.rstrip('\n') for x in file_data]

vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]

good_ctr = 0

for line in data:
    vovel_ctr = 0
    for vowel in vowels:
        vovel_ctr += line.count(vowel)

    if vovel_ctr < 3:
        continue

    last_c = ''
    c_ok = False
    
    for c in line:
        if last_c == c:
            c_ok = True
        last_c = c

    if not c_ok:
        continue

    if any(forbidden_element in line for forbidden_element in forbidden):
        continue

    good_ctr +=1

print(good_ctr)