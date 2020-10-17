#!/usr/bin/python3
import sys
import base64
import random

def encrypt(pt):
    ct = bytearray(pt, 'ascii')
    s = bytes('dummythiqq', 'ascii')

    # this part works completely in reverse
    for i in range(8):
        for j in range(len(ct)):
            ct[j] ^= s[j % len(s)] >> i
    a = 10
    b = random.randint(0, 128)
    for i in range(128):
        for j in range(len(ct)):
            ct[j] ^= a
            a = (a*2 + b) % 127
            b = (b*b) % 127

    return str(base64.b64encode(ct), 'ascii')

if __name__ == '__main__':
    print(encrypt(sys.argv[1]))
