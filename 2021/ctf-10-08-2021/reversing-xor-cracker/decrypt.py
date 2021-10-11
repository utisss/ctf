#!/usr/bin/python3
import sys
import base64

def decrypt(ciphertext):
    for b in range(128):
        ct = bytearray(ciphertext, 'ascii')
        ct = bytearray(base64.b64decode(ct))

        # Do the encryption in reverse.
        # The order of the for loops matters because the additions are dependent on previous values.
        s = bytes('optimal prime', 'ascii')
        for i in range(7, -1, -1):
            for j in range(len(ct)-1, -1, -1):
                ct[j] = (ct[j] - ct[j-1]) % 128
                ct[j] ^= s[j % len(s)] >> i

        a = 19
        for i in range(128):
            for j in range(len(ct)):
                ct[j] ^= a
                a = (a*17 + b) % 127
                b = (b*b) % 127
        

        if 'utflag' in str(ct, 'ascii'):
            return str(ct, 'ascii')
    return 'failed to decode!'

if __name__ == '__main__':
    print(decrypt(sys.argv[1]))
