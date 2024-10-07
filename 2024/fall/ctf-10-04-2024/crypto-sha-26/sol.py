import hashlib

hashes = {}

for i in range(2 ** 26):
    print(i)
    s = str(i).encode()
    hashs = f'{int(hashlib.sha256(s).hexdigest(), 16):0256b}'[:26]
    if hashs in hashes:
        print('Collision found')
        print(hashes[hashs])
        print(s)
        exit()
    hashes[hashs] = s
