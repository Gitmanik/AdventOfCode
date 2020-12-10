data_file = open('data.txt', 'r')
data = [x.replace('\n', '').split('x') for x in data_file]

sq_feet = 0
ribbon = 0

for box in data:
    box = [int(b) for b in box]

    a = box[0]*box[1]
    b = box[1]*box[2]
    c = box[2]*box[0]

    sq_feet += 2*a + 2*b + 2*c + min(a,b,c)
    ribbon += min(2*(box[0] + box[1]), 2*(box[1] + box[2]), 2*(box[2] + box[0])) + box[0]*box[1]*box[2] 
    
print(sq_feet)
print(ribbon)