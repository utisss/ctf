#!/usr/bin/env python3

from Crypto.PublicKey import RSA
import os
print('Let\'s play a game!')
print('The message space is whole numbers >= 2.')
print('Generating RSA parameters (this could take a bit...)')
key = RSA.generate(2048)
print(f'Your Verification Key:')
print(f'n = {key.n}')
print(f'e = {key.e}')

seen = []
while True:
    print('Enter a message to sign (0 to stop): ', end='')
    x = input()
    try:
        m = int(x)
        if m == 0:
            break
        if m < 2:
            print('Message must be 2 or greater.')
            os._exit(0)
        s = pow(m, key.d, key.n)
        print(f'Your signature is: {s}')
        seen.append(m)
    except:
        print('Message must be a whole number.')
        os._exit(0)

print('Now, forge a signature!')
print('Enter a new message: ', end='')
x = input()
try:
    m = int(x)
    if m < 2:
        print('Message must be 2 or greater.')
        os._exit(0)
    if m in seen:
        print('Message cannot have been previously signed by the challenger.')
        os._exit(0)
    print('Enter the signature for the message: ', end='')
    x = input()
    try:
        s = int(x)
        if s < 2:
            print('Signature must be 2 or greater.')
            os._exit(0)
        if pow(s, key.e, key.n) == m:
            print('Congratulations!')
            with open('/src/flag.txt', 'r') as f:
                print(f.read())
                os._exit(0)
        else:
            print('Signature is not valid for the message.')
            os._exit(0)
    except:
        print('Signature must be a whole number.')
        os._exit(0)
except:
    print('Message must be a whole number.')
    os._exit(0)