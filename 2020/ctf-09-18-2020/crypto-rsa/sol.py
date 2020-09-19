from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
import sage.all
from sage.arith.misc import factor

n = 829585353051679334608569297986525545433600084089844839212619
e = 3
ct = 723480078313583262942069801141894355731968051669034152256286

p,q = factor(n)
p,q = (p[0], q[0])
phi = (p - 1) * (q - 1)

d = inverse(e, phi)
pt = pow(ct, d, n)
print(long_to_bytes(pt))

