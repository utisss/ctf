# Endless Emails
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes

flag = b"utflag{????????????????????????????}"

def RSA_encrypt(message):
    m = bytes_to_long(message)
    p = getPrime(1024)
    q = getPrime(1024)
    N = p * q
    e = 3
    c = pow(m, e, N)
    return N, e, c


for i in range(3):
    N, e, c = RSA_encrypt(flag)
    print(f"n{i} = {N}")
    print(f"e{i} = {e}")
    print(f"c{i} = {c}")
    print()

