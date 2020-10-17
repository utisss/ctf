#!/usr/bin/python3
import sys
import base64

def decrypt(ciphertext):
    for b in range(128):
        ct = bytearray(ciphertext, 'ascii')
        ct = bytearray(base64.b64decode(ct))

        s = bytes('dummythiqq', 'ascii')
        for i in range(8):
            for j in range(len(ct)):
                ct[j] ^= s[j % len(s)] >> i

        a = 10
        for i in range(128):
            for j in range(len(ct)):
                ct[j] ^= a
                a = (a*2 + b) % 127
                b = (b*b) % 127
        
        if 'utflag' in str(ct, 'ascii'):
            return str(ct, 'ascii')
    return 'failed to decode!'

if __name__ == '__main__':
    print(decrypt(sys.argv[1]))
