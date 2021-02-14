from secret import key, flag
from Crypto.Util.number import bytes_to_long

def rc4(key, length):
    S = [x for x in range(256)]
    j = 0
    out = []

    for i in range(256):
        j = (j + S[i] + key[i % len(key)] ) % 256
        S[i] , S[j] = S[j] , S[i]

    i = j = 0
    while len(out) < length:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(S[(S[i] + S[j]) % 256])

    return out

s = []
for i in range(len(flag)):
    new_key = rc4(key, 100)
    x = 0
    for j in new_key:
        x ^= j
    s += [flag[i] ^ x]

print(hex(bytes_to_long(bytes(s))))
