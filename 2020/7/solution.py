file = open('data.txt', 'r')

dataset = dict()
for line in file:
    key = line[:line.index(" bag")]
    values = line[line.index(" bag") + 4:]
    values = values[values.index(" ") + len(" contain "):].rstrip('\n').rstrip('.')

    if values == "no other bags":
        dataset[key] = None
        continue

    values = [(int(x[:x.index(' ')]),x[x.index(' ')+1:x.index(" bag")]) for x in values.split(', ')]

    dataset[key] = values


searched = []

def find_bag(color):
    ctr = 0
    for key in dataset.keys():
        # print(key, dataset[key])
        if dataset[key] == None:
            continue
        for v in dataset[key]:
            if v[1] == color:
                if key not in searched:
                    ctr+=1
                    searched.append(key)
                    ctr+=find_bag(key)

    return ctr

def count(color):
    ctr = 0
    if dataset[color] == None: # Bag has no other bags inside it => it counts as 1 bag
        return 0

    for bag in dataset[color]:
        i = bag[0] + bag[0] * count(bag[1])

        print(f'{bag[0]} {bag[1]} bags contains total of {i} bags.')

        ctr +=i
    return ctr
    

print(find_bag("shiny gold"))
print(count("shiny gold"))
