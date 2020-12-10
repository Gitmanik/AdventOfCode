import hashlib

inp = "ckczppom"

ctr = 0
while True:
    ctr += 1
    md5 = hashlib.md5((inp + str(ctr)).encode('utf-8'))
    res = md5.hexdigest()
    if res.startswith("000000"):
        print(ctr, res)
        break