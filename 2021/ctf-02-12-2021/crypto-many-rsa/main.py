from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag

def encrypt(n, e, s):
    return pow(bytes_to_long(s), e, n) 

p, q, r = getPrime(256), getPrime(256), getPrime(256)
n1 = p*q
n2 = q*r
e = 65537
first = flag[:len(flag)//2]
second = flag[len(flag)//2:]

print((n1, e, encrypt(n1, e, first)))
print((n2, e, encrypt(n2, e, second)))
