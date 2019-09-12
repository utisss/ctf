
ciphertext = open('ciphertext.txt', 'r').readlines()[0]
for i in range(1, 256):
    candidate = ''.join([chr(ord(x) ^ ord(chr(i))) for x in ciphertext])
    if 'utflag' in candidate:
        print(candidate)

