from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 65537

# RSA keygen
while True:
    p = getPrime(500)
    q = p
    phi = (p**2 - p)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

n = p * q

flag = b"utflag{lol_sqrt_kinda_ez}"
pt = bytes_to_long(flag)

# RSA
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")
