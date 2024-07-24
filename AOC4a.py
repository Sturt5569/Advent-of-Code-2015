import hashlib

n = 0

while True:
    n += 1
    sample = ("ckczppom" + str(n)).encode()
    hash = hashlib.md5(sample)
    output = hash.hexdigest()

    if output.startswith("00000"):
        break
print(n)
print(output)
