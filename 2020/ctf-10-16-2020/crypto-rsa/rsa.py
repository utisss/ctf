from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 65537

# RSA keygen
while True:
    p = getprime(1000)
    q = getPrime(1000)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

n = p * q

flag = b"utflag{????????????????}"
pt = bytes_to_long(flag)

# RSA
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")
