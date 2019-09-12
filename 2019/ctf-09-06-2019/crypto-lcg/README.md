# Simplicio's Longest Calculated Game
* **Event:** BepisCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**
​

## Steps

### Step 1
We are given a file called `game.py` and we are asked to beat Simplicio's guessing game.
Simplicio's game essentialy picks a random number and in order to win we are expected to guess that number.
Inside the file we notice that there is a snippet of code that looks like this
```python
def lcg(a, c, modulus, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed

```
Some quick googling will tell us that lcg stands for [Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator).
From this we can figure out how to beat Simplicio's game.


#### Step 2
Analysing Simplicio's source code gives us the following information:
- He initializes a linear congruential generator with a random seed and a modulus of 2^64.
- The multipler and increment values are both hidden inside a file called `secret.py` that is not given to us.
- We can get as many numbers as we want from the lcg since he outputs the correct result at each guess.

From the wikipedia page linked above we know that:
 * <img src="https://latex.codecogs.com/svg.latex?X_{n&space;&plus;&space;1}&space;=&space;(aX_n&space;&plus;&space;c)&space;\mod&space;m" title="X_{n + 1} = (aX_n + c) \mod m" />


If we assume that we have already solved for the multipler `a` we can solve for `c` using two numbers from the lcg:
* <img src="https://latex.codecogs.com/svg.latex?c&space;=&space;X_{n&space;&plus;&space;1}&space;-&space;aX_n&space;\mod&space;m" title="c = X_{n + 1} - aX_n \mod m" />

In order to solve for `a` we actually need at least three numbers from the lcg. 
Notice that if we subtract two consecutive numbers we get the following equation:
* <img src="https://latex.codecogs.com/svg.latex?X_{n&space;&plus;&space;1}&space;-&space;X_n&space;=&space;a(X_n&space;-&space;X_{n&space;-1})&space;\mod&space;m" title="X_{n + 1} - X_n = a(X_n - X_{n -1}) \mod m" /> 
* <img src="https://latex.codecogs.com/svg.latex?a&space;=&space;(X_{n&space;&plus;&space;1}&space;-&space;X_n)(X_n&space;-&space;X_{n-1})^{-1}&space;\mod&space;m" title="a = (X_{n + 1} - X_n)(X_n - X_{n-1})^{-1} \mod m" />

Unfortunately since the modulus is not prime the value <img src="https://latex.codecogs.com/svg.latex?(X_n&space;-&space;X_{n-1})" title="(X_n - X_{n-1})" /> may not be [invertible](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) mod 2^64.
Using facts from elementary number theory the [Euler Totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function) computes the number of invertible elements mod m and we get that exactly 1/2 of the numbers are invertible mod m.

My solution:
``` Python
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
```


