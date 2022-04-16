from typing import List
import random

def encrypt(k: List[int], x: int):
    if len(k) != 8:
        return -1
    x_i = 1
    res = 0
    for i in range(len(k)):
        res += k[i] * x_i
        res %= 65537
        x_i *= x
    return res

flag = "utflag{redacted_redacted...}"
k = [random.randint(0, 65537) for _ in range(8)]
encrypted = [*map(lambda x: encrypt(k, ord(x)), flag)]
print(encrypted) # [57450, 16760, 17803, 15906, 7237, 36710, 52617, 44508, 16504, 33402, 17923, 16760, 16504, 33135, 19085, 7237, 50128, 44508, 19085, 17803, 33402, 17923, 16760, 16504, 33135, 19085, 15589, 7237, 16760, 17923, 50128, 36710, 19085, 59859, 57450, 33402, 33402, 17923, 16760, 16504, 33135, 19085, 40731, 17923, 16760, 15594, 19085, 44508, 7237, 50128, 50128, 41978, 19085, 44508, 15589, 48791, 17923, 16760, 16504, 28896]