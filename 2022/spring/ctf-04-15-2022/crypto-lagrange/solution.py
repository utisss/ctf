from typing import List
import string

encrypted = [57450, 16760, 17803, 15906, 7237, 36710, 52617, 44508, 16504, 33402, 17923, 16760, 16504, 33135, 19085, 7237, 50128, 44508, 19085, 17803, 33402, 17923, 16760, 16504, 33135, 19085, 15589, 7237, 16760, 17923, 50128, 36710, 19085, 59859, 57450, 33402, 33402, 17923, 16760, 16504, 33135, 19085, 40731, 17923, 16760, 15594, 19085, 44508, 7237, 50128, 50128, 41978, 19085, 44508, 15589, 48791, 17923, 16760, 16504, 28896]
M = 65537

known = [*map(lambda x: ord(x), "utflag{}")]
known_encrypted = encrypted[:7] + [encrypted[-1]]

#adapted from https://www.codesansar.com/numerical-methods/python-program-lagrange-interpolation-method.htm
def interpolate(x: List[int], y: List[int], xp: int):
    yp = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (xp - x[j]) * pow(x[i] - x[j], -1, M)
                p %= M
        yp += p * y[i]
        yp %= M
    return yp

interpolations = [interpolate(known, known_encrypted, i) for i in range(256)]
inv_interps = {}
for c in string.printable:
    i = ord(c)
    inv_interps[interpolations[i]] = i

res = ""
for e in encrypted:
    res += chr(inv_interps[e])
print(res)