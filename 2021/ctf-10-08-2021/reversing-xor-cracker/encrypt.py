#!/usr/bin/python3
import sys
import base64
import random

def encrypt(pt):
    ct = bytearray(pt, 'ascii')
    s = bytes('optimal prime', 'ascii')

    a = 19
    b = random.randint(0, 128)
    for i in range(128):
        for j in range(len(ct)):
            ct[j] ^= a
            a = (a*17 + b) % 127
            b = (b*b) % 127

    for i in range(8):
        for j in range(len(ct)):
            ct[j] ^= s[j % len(s)] >> i
            ct[j] = (ct[j] + ct[j-1]) % 128

    return str(base64.b64encode(ct), 'ascii')

if __name__ == '__main__':
    print(encrypt(sys.argv[1]))
