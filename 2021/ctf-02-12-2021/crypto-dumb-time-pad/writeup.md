In the code, we can see that the value used to xor every byte in the flag stays the same, since the key is never set to the new key.
Thus, we can just brute force all 256 possible bytes that were used to xor:
```
from Crypto.Util.number import long_to_bytes

enc = long_to_bytes(0xc3c2d0dad7d1cddfe9d086c4d186c2e984e9c48583d3c2e9c2de85e9c58585d2cb)

for byte in range(256):
    flag = bytes([x ^ byte for x in enc])
    if b'utflag' in flag:
        print(flag)
```
