# The random number generator uses the LCG algorithm.

# Necessary modular arithmetic math from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b
    else:
        return -1

def find_increment(x0, x1, m, a):
    c = (x1 - x0 * a) % m
    return a, c

def find_multiplier(x0, x1, x2, m):
    inv = mulinv(x1 - x0, m)
    # x1 - x0 is not invertible in this case
    if(inv == -1):
        return -1
    a = (x2 - x1) * inv % m
    return find_increment(x0, x1, m, a)


# Note: These values come from some fixed seed.
# We may need more than 3 values since x1 - x0 is not always guaranteed to be invertible mod 2^64.

values = [939990531185586193, 293603765658411854, 5975095473608304647, 17267424818825692044, 11387026378546418925, 3575682438720176634, 6610569397993644099]
m = 1 << 64

for i in range(len(values) - 3):
    res = find_multiplier(values[i], values[i+1], values[i+2], m)
    if res != -1:
        a, c = res[0], res[1]
        print((values[-1] * a + c) % m)
        break






