from Crypto.Util.number import *
from secret import flag

p,q = getPrime(256), getPrime(256)
e = 65537
n = p * q

plaintext = bytes_to_long(flag)
ciphertext = pow(plaintext, e, n)
print(ciphertext)
print(n)
print(p+q)

