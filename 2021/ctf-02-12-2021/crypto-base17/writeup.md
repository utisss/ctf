Trying to decode the flag using base 16 yields gibberish, since the flag is actually encoded in base 17.
We can write python code to decode it, as follows:

```
from Crypto.Util.number import long_to_bytes

def get(x):
    if ord('0') <= x and x <= ord('9'):
        return x - ord('0')
    else:
        return x - ord('a') + 10


enc = '5b60807e447c469360c6b5a1a29ba681ebcfa2e5134f9a648ff'

num = 0
for x in enc:
    num = num*17 + get(ord(x))

print(long_to_bytes(num))
```
