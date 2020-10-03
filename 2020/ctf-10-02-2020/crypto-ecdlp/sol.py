from sage.all import *
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

FLAG = b'utflag{pq}'

a,b,q = (284470887156368047300405921324061011681, -4414881994420432611408289453530435152719356090172935739362871971003124023085868425834905919486013443094617738800944, 340282366762482138434845932242542250033)
R = Zmod(q)
E = EllipticCurve(R, [a, b])
G = E(0x7b6aa5d85e572983e6fb32a7cdebc140, 0x27b6916a894d3aee7106fe805fc34b44)
P = G*bytes_to_long(FLAG)

print(P)

dlogs = []
orders = []
for f in factor(q):
    m = f[0]**f[1]
    F_ = GF(m, 'z')
    E_ = EllipticCurve(F_, [a,b])
    dlogs.append(discrete_log(E_(P),E_(G),operation="+"))
    orders.append(E_(G).order())

print(long_to_bytes(crt(dlogs, orders)))
